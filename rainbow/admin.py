from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(property_table)
admin.site.register(property_image)
admin.site.register(user_image)
admin.site.register(transaction_details)
admin.site.register(purchase_rental_table)
admin.site.register(news_information)