from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
# from .models import views


from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def index(response):
    return HttpResponse("eawr")
    
def register(request):
    if request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/main/")
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user) 
                return redirect('login')


    context = {'form': form}
    return render(request, 'register/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/main/")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/main/')
            else:
                messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'register/login.html', context)

def logoutUser(request): 
    logout(request)
    return redirect('login')

    
