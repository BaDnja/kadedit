from django.shortcuts import render, redirect


def index(request):
    """Handle displaying landing page of the application."""
    if request.user.is_authenticated:
        return redirect('professors')
    return render(request, "pages/index.html")
