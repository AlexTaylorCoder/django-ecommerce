from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Comment(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default="",null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="",null=True,blank=True)
    #Needs through relationship, look more into django set relationships
    #Need foreign key for user here also
