from django.shortcuts import render


def subjects(request):
    """Handle processing main page for professors"""
    return render(request, 'subjects/dashboard-subjects.html')
