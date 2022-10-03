from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User 

from embed_video.fields import EmbedVideoField

class Product(models.Model):
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    miniDescription = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=400,null=True,blank=True)
    url = EmbedVideoField(null=True,blank=True)

    #Need foreign key for user here also
