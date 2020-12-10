from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def user_login(request):
    """Handle user authentication and login"""
    if request.method == 'POST':
        form = forms.LoginForm()
        if form.is_valid():
            #TODO: add form to the template using widget tweak
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('professors')
            else:
                return redirect('user_login')
        else:
            return redirect('user_login')

    return render(request, 'accounts/login.html')


def user_logout(request):
    """Handle logging out current user"""
    logout(request)
    return redirect('user_login')
