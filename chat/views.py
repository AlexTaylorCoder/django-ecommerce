from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'chat/home.html',{})

def room(request,room_name):
    return render(request,'chat/chatroom.html', {'id':room_name})