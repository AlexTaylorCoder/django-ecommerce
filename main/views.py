from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from .forms import CreateNewProduct

from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def index(response):
    products = {"products":Product.objects.all()}
    return render(response, 'main/products.html',products)
def show(response,id):
    product = {"product":Product.objects.get(pk=id)}
    return render(response,'main/product.html',product)

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def create(response):
    if response.method == "POST":
        form = CreateNewProduct(response.POST, response.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"] 
            price = form.cleaned_data["price"]
            image = form.cleaned_data["image"]
            product = Product.objects.create(name=name,price=price,image=image)
        return HttpResponseRedirect(f'{product.id}')
    else:
        form = CreateNewProduct()
    return render(response,'main/create.html',{"form":form})
