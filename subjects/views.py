from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from . import models


def subjects(request):
    """Handle getting main page for professors"""
    if request.user.is_authenticated:
        all_subjects = models.Subject.objects.filter(active=True)

        paginator = Paginator(all_subjects, 25)
        page = request.GET.get('page')

        try:
            paged_subjects = paginator.get_page(page)
        except PageNotAnInteger:
            paged_subjects = paginator.page(1)
        except EmptyPage:
            paged_subjects = paginator.page(paginator.num_pages)

        context = {
            'obj_list': paged_subjects,
        }

        return render(request, 'subjects/dashboard-subjects.html', context)
    else:
        return redirect('user_login')


def subject(request, subject_id):
    """Handle getting single subject"""
    if request.user.is_authenticated:
        subj = get_object_or_404(models.Subject, pk=subject_id)
        context = {
            'subject': subj
        }

        return render(request, 'subjects/subject.html', context)
    else:
        return redirect('user_login')
