from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def index(request):   
        return render(request,'chat/home.html',{'eaat':'awtawts'})

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def room(request,room_name):
        return render(request,'chat/chatroom.html', {'room_name':room_name})

# @login_required(login_url='http://127.0.0.1:8000/auth/login/')
# def create(request):
#     return render(request)
#     Needs form that on response.method = POST creates new room 



