from django import forms
master_bedroom = ((True, 'has master bedroom'),
 (False, 'does not have master bedroom'))
class registration_form(forms.Form):
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
      'id' : 'first_name',
     'class':'form-control',
     'placeholder':'enter first name'
      }))
    second_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
      'id' : 'second_name',
     'class':'form-control',
      'placeholder':'enter second name'}))
    signupemail = forms.EmailField(widget = forms.EmailInput(attrs={
      'id' : 'signupemail',
     'class':'form-control',
      'placeholder':'enter email'}))
    street_address = forms.CharField(max_length=250, widget = forms.TextInput(attrs={
      'id' : 'address',
     'class':'form-control',
      'placeholder':'enter street name and apartment number'}))
    city = forms.CharField(max_length=250, widget = forms.TextInput(attrs={
      'id' : 'city',
     'class':'form-control',
      'placeholder':'enter city'}))
    zip_code = forms.CharField(max_length=20, widget = forms.TextInput(attrs={
      'id' : 'zip_code',
     'class':'form-control',
      'placeholder':'enter zip code'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs = {
      'id': 'phonenumber',
      'class':'form-control',
      'placeholder' : 'enter phone number'

    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
      'id' : 'signuppassword',
     'class':'form-control',
      'placeholder':'enter password'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
      'id' : 'images-field',
     'class':'form-control',
    }))



class login_form(forms.Form):
  email = forms.EmailField(widget = forms.EmailInput(attrs={'id' : 'signupemail',
  'class':'form-control',
  'placeholder':'enter email'}))

  password = forms.CharField(widget = forms.PasswordInput(attrs={'id' : 'signuppassword',
     'class':'form-control',
      'placeholder':'enter password'}))



class properties_form(forms.Form):
    property_title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'id' : 'property_title',
     'class':'form-control',
     'placeholder':'enter property title'
      }))

    property_description = forms.CharField(widget=forms.Textarea(attrs={'id' : 'property_description',
     'class':'form-control',
      'placeholder':'enter property description'}))

    price = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'property_price',
     'class':'form-control',
      'placeholder':'enter price'}))

    no_of_rooms = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'no_of_rooms',
     'class':'form-control',
      'placeholder':'enter number of rooms'}))

    furniture_type = forms.CharField(max_length=250, widget = forms.TextInput(attrs={'id' : 'furniture_type',
     'class':'form-control',
      'placeholder':'enter type of furniture'}))

    number_of_resident = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'number_of_resident',
     'class':'form-control',
      'placeholder':'enter number of resident'}))

    kitchen_and_other_appliance = forms.CharField(max_length=200, widget = forms.TextInput(attrs={'id' : 'kitchen_and_other_appliance',
     'class':'form-control',
      'placeholder':'enter other appliances'}))

    has_master_bedroom = forms.BooleanField(widget=forms.Select(attrs = {
      'id': 'has_master_bedroom',
      'class':'form-control',
      'placeholde' : 'has master bedroom',

    }, choices = master_bedroom))

    dinning_seat = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'dinning_seat',
     'class':'form-control',
      'placeholder':'enter number of dinning seat'}))

    no_of_car_in_parking = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'no_of_car_in_parking',
     'class':'form-control',
      'placeholder':'how large is parking space'}))

    no_of_guest_toilet = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'no_of_guest_toilet',
     'class':'form-control',
      'placeholder':'ente number of guest toilet'}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'id' : 'images-field',
     'class':'form-control',
     'multiple' : True,
    },))


  
