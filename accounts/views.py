from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    """Handle user authentication and login"""
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Uspješna prijava")
                return redirect('professors')
            else:
                messages.error(request, "Neuspjela prijava")
                return redirect('user_login')
    else:
        return redirect('professors')

    return render(request, 'accounts/login.html')


def user_logout(request):
    """Handle logging out current user"""
    logout(request)
    messages.success(request, "Uspješna odjava")
    return redirect('user_login')
