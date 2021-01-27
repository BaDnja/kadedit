from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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


def work_statuses(request):
    """Handles getting page for listing all work statuses in the system."""
    if request.user.is_authenticated:
        all_work_statuses = models.WorkStatus.objects.all().order_by('id')

        paginator = Paginator(all_work_statuses, 10)
        page = request.GET.get('page')

        try:
            paged_statuses = paginator.get_page(page)
        except PageNotAnInteger:
            paged_statuses = paginator.page(1)
        except EmptyPage:
            paged_statuses = paginator.page(paginator.num_pages)

        context = {
            'statuses': paged_statuses,
        }

        return render(request, 'professors/work_statuses.html', context)
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def single_work_status(request, status_id):
    if request.user.is_authenticated:
        if request.user.has_perm("professors.view_workstatus"):
            status = get_object_or_404(models.WorkStatus, pk=status_id)
            context = {
                'status': status,
            }
            return render(request, 'professors/single_work_status.html', context)
        else:
            messages.error(request, "Niste ovlašteni za pregled radnog statusa")
            return redirect('work_statuses')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def work_status_add(request):
    if request.user.is_authenticated:
        if request.user.has_perm("professors.add_workstatus"):
            if request.method == 'POST':
                name = request.POST['Name']

                if models.WorkStatus.objects.filter(name=name).exists():
                    messages.error(request, "Status već postoji")
                    return redirect('work_status_add')
                else:
                    status = models.WorkStatus(name=name)
                    status.save()
                    messages.success(request, "Uspješno dodan status")
                    return redirect('work_statuses')
            return render(request, 'professors/work_status_add.html')
        else:
            messages.error(request, "Nemate ovlaštenje za dodavanje radnog statusa")
            return redirect('work_statuses')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def work_status_update(request, status_id):
    status = get_object_or_404(models.WorkStatus, pk=status_id)
    if request.user.has_perm("professors.change_workstatus"):
        if request.method == 'POST':
            status.name = request.POST.get("Name")
            status.save()
            messages.success(request, "Uspješna izmjena")
            return redirect('single_work_status', status_id=status_id)
    else:
        messages.error(request, "Nemate ovlaštenje za izmjenu radnog statusa")
        return redirect("work_statuses")


def work_status_delete(request, status_id):
    status = get_object_or_404(models.WorkStatus, pk=status_id)
    if request.user.has_perm("professors.delete_workstatus"):
        if request.method == 'POST':
            status.delete()
            messages.success(request, "Uspješno obrisan status")
            return redirect('work_statuses')
    else:
        messages.error(request, "Nemate ovlaštenje za brisanje radnog statusa")
        return redirect('single_work_status', status_id=status_id)
