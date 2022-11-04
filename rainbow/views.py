from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import registration_form, login_form, properties_form
from .models import *
import re
import uuid
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.core.signing import Signer
from asgiref.sync import sync_to_async
import threading
from .details_email import email_message
from django.contrib import messages
from django.http import request

# Create your views here.

def home_page(request):
    context = {

    }
    if request.user.is_authenticated :
        user_img = user_image.objects.get(property_id=request.user)
        context = {
                'user_image' : user_img
            }
    return render(request, 'rainbow/index.html', context)

def about_page(request):
    return render(request, 'rainbow/about.html')

def contact_page(request):
    return render(request, 'rainbow/contact.html')

def all_properties_page(request):
    return render(request, 'rainbow/property.html')

def single_properties_page(request):
    return render(request, 'rainbow/property-single.html')

def profile_page(request):
    return render(request, 'rainbow/profile.html')

def admin_dashboard(request):
    #checking if form is sent, and getting the from data
    if request.method == "POST":
        form = properties_form(request.POST, request.FILES)

        #checking if the input of the form are valid and retrieving the cleaned data
        id = uuid.uuid1()
        if form.is_valid() :
            property_title = form.cleaned_data("property_title")
            property_description = form.cleaned_data("property_description")
            price = form.cleaned_data("price")
            no_of_rooms = form.cleaned_data("no_of_rooms")
            furniture_type = form.cleaned_data("furniture_type")
            number_of_resident = form.cleaned_data("number_of_resident")
            kitchen_and_other_appliance = form.cleaned_data("kitchen_and_other_appliance")
            has_master_bedroom = form.cleaned_data("has_master_bedroom")
            dinning_seat = form.cleaned_data("dinning_seat")
            no_of_car_in_parking = form.cleaned_data("no_of_car_in_parking")
            no_of_guest_toilet = form.cleaned_data("no_of_guest_toilet")
            images = request.FILES.getlist('image')

            try :
                property = property_table(property_id=id, property_title=property_title, property_descriptions=property_description,
                price=price, image_count=len(images), no_of_rooms=no_of_rooms, furniture_type=furniture_type,
                number_of_residents=number_of_resident,  kitchen_and_other_appliance=kitchen_and_other_appliance,
                has_master_bedroom=has_master_bedroom, dinning_seat=dinning_seat, no_of_car_in_parking=no_of_car_in_parking,
                no_of_guest_toilet=no_of_guest_toilet)
            except:
                messages.error(request, "content does not correspoand to database input")

            else:
                property.save()

                for image in images:
                    image_data = property_image(property_id=property, image=image)
                    image_data.save()
                    
                messages.success(request, "content successfully save")

                print(f"""
                property_title : {property_title} \n
                property_description : {property_description} \n
                price : {price} \n
                no_of_rooms : {no_of_rooms} \n
                kitchen_and_other_appliance : {kitchen_and_other_appliance} \n
                furniture_type : {furniture_type} \n
                has_master_bedroom : {has_master_bedroom} \n
                """)
                #etting the image

                for image in images:
                    print(image)

    else :
        form = properties_form()
        context = {
            'form' : form
        }
    return render(request, 'rainbow/admin-dashboard.html', context)

def login_user(request):
    login_forms = login_form()
    context = {
            'log_form' : login_forms
        }
    if request.method == 'POST':
        login_forms = login_form(request.POST)

        if login_forms.is_valid():
            email = login_forms.cleaned_data['email']
            password = login_forms.cleaned_data["password"]

            try:
                user = authenticate(email=email, password=password)

            except :
                print("user not found")
                messages.error(request, "login credetials are not correct")
        if user is not None :
            login(request, user)
            return redirect(home_page)
    return render(request, 'rainbow/login.html', context)

def signup(request):
    form = registration_form()
    context = {'signupform' : form,
    'error' : "",
    }
    id = uuid.uuid1()
    if request.method == 'POST' :
        register_form = registration_form(request.POST, request.FILES)
        if register_form :
            print("Form input received")
        if register_form.is_valid():
            first_name = register_form.cleaned_data['first_name']
            second_name = register_form.cleaned_data['second_name']
            signupemail = register_form.cleaned_data['signupemail']
            street_address = register_form.cleaned_data['street_address']
            zip_code = register_form.cleaned_data['zip_code']
            phone_number = register_form.cleaned_data['phone_number']
            password = register_form.cleaned_data['password']
            city = register_form.cleaned_data['city']
            image = register_form.cleaned_data['image']
            user_id = str(first_name + str(id))

            check_email = CustomUser.objects.filter(email=signupemail)

            if not check_email :

            # =========== signed data ==============
                signer = Signer()

                signed_email = signer.sign(signupemail)
                signed_password = signer.sign(password)

                user_details = CustomUser(user_id= user_id.lower(), first_name=first_name,
                last_name=second_name, email=signupemail, phone_number=phone_number, zip_code = zip_code,
                street_address=street_address, city=city, username=str(first_name + second_name))


                user_details.set_password(password)

                user_details.save()
                image_details = user_image(property_id = user_details, image=image)
                image_details.save()

                # ======================== preparing email data =================
                home_url =  request.get_full_path()
                absolute_link = str(home_url + f"?email={signed_email}?pass={signed_password}")
                absolute_image = f"{image}"
                
                # html_message = email_message(absolute_link, absolute_image, user_id, str(first_name + " " + second_name),
                #  country, password, signed_email)
                send_email = threading.Thread(target=email_message, args=(absolute_link, absolute_image, user_id, str(first_name + " " + second_name),
                password, signed_email))

                print("email is sending ========")
                send_email.start()
                return redirect(login_user)
            else :
                messages.error(request, "email is not correct")
                return redirect(signup)

        else :
            print(register_form.errors)
            context['error'] = "form is not valid check input carefully"

    return render(request, 'rainbow/signup.html', context)