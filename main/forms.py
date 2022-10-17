from dataclasses import fields
from django import forms 
from django.forms import ModelForm, widgets
from .models import Product, Comment

class CreateNewProduct(forms.Form):
    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits = 8, decimal_places = 2)
    description = forms.CharField(max_length=400, required=False)
    image = forms.ImageField(required=False)
     # miniDescription = forms.CharField(max_length=200, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'}),
        self.fields['price'].widget.attrs.update({'class':'form-control'}),
        self.fields['description'].widget.attrs.update({'class':'form-control'}),
        self.fields['image'].widget.attrs.update({'class':'form-control'})

   

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'}),
        self.fields['price'].widget.attrs.update({'class':'form-control'}),
        self.fields['description'].widget.attrs.update({'class':'form-control'}),
        self.fields['image'].widget.attrs.update({'class':'form-control'})


class CreateComment(ModelForm):
    class Meta:
        labels = {
            "text":"Comment"
        }
        model = Comment
        fields = ["text","rating"]

