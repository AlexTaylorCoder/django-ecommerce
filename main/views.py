from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import *
from .forms import CreateNewProduct, CreateComment
from django.contrib.auth.models import User 
from django.http import JsonResponse
import json
import datetime
from audioop import avg
from django.db.models import Avg, Count
from django.urls import reverse
                             

from .forms import ProductForm

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

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    products = {"products":Product.objects.all(), "cart_Items":cart_Items}
    return render(response, 'main/products.html',products)

def show(response,id):
    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

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

    product = {"product": p, "comments":comment, "comments_length":comment.count(), "room_name":id, "cart_Items":cart_Items}
    if comment.count() > 0:
        avg_rating = comment.aggregate(Avg('rating'))
        avg_rating_format = '{0:.2f}'.format(avg_rating["rating__avg"])
        product["avg_rating"] = avg_rating_format
        
    if check_if_comm is False:
        product["form"] = CreateComment()
    return render(response,'main/product.html',product)




@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def create(response):

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    if response.method == "POST":
        form = CreateNewProduct(response.POST, response.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"] 
            price = form.cleaned_data["price"]
            image = form.cleaned_data["image"]
            # miniDescription = form.cleaned_data["miniDescription"]
            description = form.cleaned_data["description"]
            product = Product.objects.create(name=name,price=price,image=image,description=description)

        return HttpResponseRedirect(f'{product.id}')
    else:
        form = CreateNewProduct()

    context = {"form":form, "cart_Items":cart_Items}
    return render(response,'main/create.html',context)



@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def updateProduct(response,id):

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    product = get_object_or_404(Product, id = id)
    form = ProductForm(response.POST or None, instance = product)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'http://127.0.0.1:8000/main/{product.id}')
 
    context={"form":form, "cart_Items":cart_Items}
    return render(response, 'main/update.html', context)

    

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def deleteProduct(response,id):

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    context ={"cart_Items":cart_Items}
    product = get_object_or_404(Product, id = id)

    if response.method == 'POST':
        product.delete()
        return redirect('http://127.0.0.1:8000/main')
        
    return render(response, 'main/delete.html', context)

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def profile(response):
    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items
    context={'cart_Items':cart_Items}
    return render(response, 'main/profile.html', context)

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def cart(response):

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    if response.user.is_authenticated:
        customer = response.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
    context={'items':items, 'order':order, "cart_Items":cart_Items}
    return render(response, 'main/cart.html', context)

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def checkout(response):

    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    if response.user.is_authenticated:
        customer = response.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else: 
        items = []
    context={'items':items, 'order':order, "cart_Items":cart_Items}
    return render(response, 'main/checkout.html', context)



@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def updateItem(response):
    data = json.loads(response.body)
    productId = data["productId"]
    action = data["action"]

    print("Action:", action)
    print("productId:", productId)

    customer = response.user
    # product = get_object_or_404(Product, id = productId)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
  
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1 )
   
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(response):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(response.body)

    customer = response.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id 

    order.complete = True 
    if order.complete == True:
        order.date_ordered = datetime.datetime.now()
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )
    return JsonResponse("Payment complete", safe= False)


def orders(response):
    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items
    context = {"user_orders":response.user.order_set.all().order_by('-date_ordered').values(), "cart_Items":cart_Items}

    return render(response, 'main/orders.html', context)


def order_details(response,id):
    
    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    order = Order.objects.get(id=id)
    items = order.orderitem_set.all()
    shipping_address = order.shippingaddress_set.all()
    context = {"order":order, "items":items, "shipping_address":shipping_address, "cart_Items":cart_Items}
    return render(response, 'main/order_details.html', context)
    

def delete_orderitem(response,id):
    orders = response.user.order_set.all()
    cart_Items = 0
    for order in orders:
        if order.complete == False:
            cart_Items = order.get_cart_items

    context ={"cart_Items":cart_Items}
    item = get_object_or_404(OrderItem, id = id)

    ord = 0
    for order in orders:
        for orderitem in order.orderitem_set.all():
            if orderitem.id == id:
                ord = order.id

    if response.method == 'POST':
        item.delete()
        return redirect(f'http://127.0.0.1:8000/main/order_details/{ord}')
        
    return render(response, 'main/delete.html', context)


