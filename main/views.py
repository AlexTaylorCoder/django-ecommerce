from audioop import avg
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CreateNewProduct, CreateComment
from .forms import ProductForm
from django.db.models import Avg, Count
from django.urls import reverse

from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def like_comment(response,pk):
    comment = get_object_or_404(Comment, id=response.POST.get('like-id'))
    # breakpoint()
    comment.likes.add(response.user)
    return HttpResponseRedirect(reverse('show', args = [str(pk)]))

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def index(response):
    products = {"products":Product.objects.all()}
    return render(response, 'main/products.html',products)
def show(response,id):
    if response.method == "POST" and response.user.is_authenticated:
        form = CreateComment(response.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = response.user
            new_comment.product = Product.objects.get(pk=id)
            new_comment.save()

    p = Product.objects.get(pk=id)
    c =  p.comment_set.all()
    check_if_comm = c.filter(user=response.user).exists()
    comment = c.annotate(Count('likes'))    

    product = {"product": p, "comments":comment, "comments_length":comment.count(), "room_name":id}
    if comment.count() > 0:
        avg_rating = comment.aggregate(Avg('rating'))
        avg_rating_format = '{0:.2f}'.format(avg_rating["rating__avg"])
        product["avg_rating"] = avg_rating_format
        
    if check_if_comm is False:
        product["form"] = CreateComment()
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
