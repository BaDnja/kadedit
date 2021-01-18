from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from . import models


def professors(request):
    """Handle getting main page for professors"""
    if request.user.is_authenticated:
        all_professors = models.Professor.objects.filter(active=True).order_by('-id')

        paginator = Paginator(all_professors, 15)
        page = request.GET.get('page')

        try:
            paged_professors = paginator.get_page(page)
        except PageNotAnInteger:
            paged_professors = paginator.page(1)
        except EmptyPage:
            paged_professors = paginator.page(paginator.num_pages)

        context = {
            'obj_list': paged_professors,
        }
        return render(request, 'professors/dashboard-professors.html', context)
    else:
        return redirect('user_login')


def professor(request, professor_id):
    """Handle getting single page for professor"""
    if request.user.is_authenticated:
        prof = get_object_or_404(models.Professor, pk=professor_id)
        context = {
            'professor': prof
        }

        return render(request, 'professors/professor.html', context)
    else:
        return redirect('user_login')
