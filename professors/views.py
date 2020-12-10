from django.shortcuts import render


def professors(request):
    """Handle processing main page for professors"""
    return render(request, 'professors/dashboard-professors.html')
