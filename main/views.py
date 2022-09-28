from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from .forms import CreateNewProduct
# Create your views here.
def index(response):
    products = {"products":Product.objects.all()}
    return render(response, 'main/products.html',products)
def show(response,id):
    product = {"product":Product.objects.get(pk=id)}
    return render(response,'main/product.html',product)
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
