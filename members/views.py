from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


def home(request):
    return render(request, 'authentication/home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There was a mistake try again"))
            return redirect('login')
    
    else:
        return render(request, 'authentication/login.html', {})

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,('Registration successful'))
            return redirect('home')
    else:
        form= RegisterUserForm()
    return render(request, 'authentication/register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, ("You logged out"))
    return redirect('home')
