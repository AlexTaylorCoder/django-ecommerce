from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User 

from email.policy import default
from enum import unique
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

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property 
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=2000, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Comment(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    text = models.CharField(max_length=400)
    likes = models.ManyToManyField(User, related_name="comment_like")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default="",null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="",null=True,blank=True)
    #Needs through relationship, look more into django set relationships
    #Need foreign key for user here also
    def total_likes(self):
        return self.likes.count()