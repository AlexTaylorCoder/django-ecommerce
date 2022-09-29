from django.shortcuts import render, HttpResponse, redirect

def index(request):   
        render(request,'chat/home.html',{})

def room(request,room_name):
        return render(request,'chat/chatroom.html', {'room_name':room_name})


