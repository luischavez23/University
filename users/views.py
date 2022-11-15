from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

def signup_user(request):
    form = UserCreationForm()
    if request.method != 'POST':
        return render(request, 'user/signup_user.html', {'form':form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError: 
                return render(request, 'user/signup_user.html', {'form':form, 'error': 'The username has already been used.'})
        else:
            return render(request, 'user/signup_user.html', {'form':form, 'error': 'Passwords did not match.'})

def login_user(request):
    form = AuthenticationForm()
    if request.method != 'POST':
        return render(request, 'user/login_user.html', {'form':form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'user/login_user.html', {'form':form, 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
