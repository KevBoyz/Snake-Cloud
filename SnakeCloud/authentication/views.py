from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants


def register(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.ERROR, 'Logout to access this page')
        return redirect('/')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            user = User.objects.create_user(username=name, email=email,
                                            password=password1, is_active=True)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'User registered')
            return redirect('auth/login.html')
        except Exception as e:
            messages.add_message(request, constants.ERROR, e)
            return render(request, 'auth/register.html')
    elif request.method == 'GET':
        return render(request, 'auth/register.html')


def login(request):
    if request.user.is_authenticated:
        messages.add_message(request, constants.ERROR, 'Logout to access this page')
        return redirect('/')

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        if not user:
            messages.add_message(request, constants.ERROR, 'Username or password incorrect')
            return render(request, 'auth/login.html')
        else:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logged successfully')
            return redirect('/')

    elif request.method == 'GET':
        return render(request, 'auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
