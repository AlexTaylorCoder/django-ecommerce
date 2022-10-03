from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Product
from .forms import CreateNewProduct


                             

from .forms import ProductForm

from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def index(response):
    products = {"products":Product.objects.all()}
    return render(response, 'main/products.html',products)
def show(response,id):
    product = {"product":Product.objects.get(pk=id), "room_name":id}
    return render(response,'main/product.html',product)


@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def create(response):
    if response.method == "POST":
        form = CreateNewProduct(response.POST, response.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"] 
            price = form.cleaned_data["price"]
            image = form.cleaned_data["image"]
            miniDescription = form.cleaned_data["miniDescription"]
            description = form.cleaned_data["description"]
            product = Product.objects.create(name=name,price=price,image=image,miniDescription=miniDescription,description=description)

        return HttpResponseRedirect(f'{product.id}')
    else:
        form = CreateNewProduct()
    return render(response,'main/create.html',{"form":form})



@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def updateProduct(response,id):

    context ={}

    product = get_object_or_404(Product, id = id)
    form = ProductForm(response.POST or None, instance = product)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'http://127.0.0.1:8000/main/{product.id}')
 
    context["form"] = form
    return render(response, 'main/update.html', context)

    

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def deleteProduct(response,id):
    context ={}
    product = get_object_or_404(Product, id = id)

    if response.method == 'POST':
        product.delete()
        return redirect('http://127.0.0.1:8000/main')
        
    return render(response, 'main/delete.html', context)

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def profile(response):
    return render(response, 'main/profile.html',{"user":response.user})




# @login_required(login_url='http://127.0.0.1:8000/auth/login/')
# def updateProduct(response,id):

#     context ={}

#     product = get_object_or_404(Product, id = id)
#     form = ProductForm(response.POST or None, instance = product)

#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(f'http://127.0.0.1:8000/main/{product.id}')
 
#     context["form"] = form
#     return render(response, 'main/update.html', context)



# @login_required(login_url='http://127.0.0.1:8000/auth/login/')
# def create(response):
#     context ={}
 
#     # add the dictionary during initialization
#     form = ProductForm(response.POST or None)
#     if form.is_valid():
#         form.save()
         
#     context['form']= form
#     return render(response, "main/update.html", context)
