from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    #Need foreign key for user here also
