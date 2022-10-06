from django import forms 
from django.forms import ModelForm
from .models import Product

class CreateNewProduct(forms.Form):
    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits = 8, decimal_places = 2)
    image = forms.ImageField(required=False)
    miniDescription = forms.CharField(max_length=200, required=False)
    description = forms.CharField(max_length=400, required=False)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

