# Create your views here.
# from problems import forms
import users
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserRegistrationForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login')


def login_view(request):
    form = AuthenticationForm(request.POST, 'user')
    if form.is_valid():
        username_var = request.POST.get('username')
        password_var = request.POST.get('password')
        user = authenticate(request, username=username_var, password=password_var)
        if user:
            login(request, user)
            return redirect('/')
        context = {"form": form}
        return render(request, 'auth/login.html', context)
