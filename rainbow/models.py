from django.db import models
from PIL import Image

# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
transaction_stete = (("F", "Fail"),
    ("S", "Success")
)
voting_status = (("S", "Sell"),
    ("B", "Buy"))

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length = 200, primary_key = True, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(null = True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    is_verified = models.BooleanField(default = False)
    register_date = models.DateTimeField(auto_now_add = True)
    zip_code = models.CharField(max_length=50)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'password', 'last_name', 'username']

class property_table(models.Model):
    property_id = models.CharField(max_length = 200, primary_key = True)
    property_title = models.CharField(max_length = 150)
    property_descriptions = models.TextField()
    price = models.IntegerField()
    date_uploaded = models.DateTimeField(auto_now = True)
    date_modified = models.DateTimeField(auto_now_add = True)
    image_count = models.IntegerField()
    no_of_rooms = models.IntegerField()
    furniture_type = models.CharField(max_length = 250, null = True)
    number_of_residents = models.IntegerField(null=True)
    kitchen_and_other_appliance = models.CharField(max_length = 250, null=True)
    has_master_bedroom = models.BooleanField(default=False)
    dinning_seat = models.IntegerField(null=True)
    no_of_car_in_parking = models.IntegerField(null=True)
    no_of_guest_toilet = models.IntegerField(null=True)
    


    class Meta :
        db_table = "property_table"
    

class property_image(models.Model):
    property_id = models.ForeignKey(property_table, on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='property_image', default="property.jpg")

    class Meta :
        db_table = "property image"

class user_image(models.Model):
    property_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='user_image', default='user.jpg')

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (70, 70)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta :
        db_table = "user image table"


class transaction_details(models.Model):
    tanscation_id = models.CharField(max_length=200, primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property_id = models.ForeignKey(property_table, on_delete=models.CASCADE)
    ammount_invested = models.IntegerField()
    date_purchased = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=4, choices=transaction_stete)

    class Meta :
        db_table = "user details table"

class purchase_rental_table(models.Model):
    purchase_id = models.CharField(max_length=200, primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property_id = models.ForeignKey(property_table, on_delete=models.CASCADE)
    ammount_invested = models.IntegerField()
    date_invested = models.DateTimeField(auto_now_add=True)
    property_transaction_id = models.ForeignKey(transaction_details, on_delete=models.CASCADE)

    class Meta :
        db_table = "investment table"


class news_information(models.Model):
    news_topic = models.CharField(max_length=250)
    news_content = models.TextField()
    date_published = models.DateTimeField(auto_now = True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta :
        db_table = "news information table"

