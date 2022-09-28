from django import forms 

class CreateNewProduct(forms.Form):
    name = forms.CharField(max_length=20)
    price = forms.DecimalField(max_digits = 8, decimal_places = 2)
    image = forms.ImageField(required=False)