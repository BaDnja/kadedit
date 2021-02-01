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
        messages.error(request, "Prijavite se na sistem")
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
    """
    Handles getting page for listing all work statuses in the system.
    Function check if request user is authenticated. If not, it redirects the user to the login page.
    If user is authenticated, it creates pagination and lists all work statuses for that pagination page.
    """
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

        return render(request, 'professors/work_statuses/work_statuses.html', context)
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def single_work_status(request, status_id):
    """
    Handles listing single work status for given status id.
    Function checks if user is authenticated and has permission to view status. If user is not authenticated
    or doesn't have permission to view status, system redirects request user to other pages with corresponding messages.
    """
    if request.user.is_authenticated:
        if request.user.has_perm("professors.view_workstatus"):
            status = get_object_or_404(models.WorkStatus, pk=status_id)
            context = {
                'status': status,
            }
            return render(request, 'professors/work_statuses/single_work_status.html', context)
        else:
            messages.error(request, "Niste ovlašteni za pregled radnog statusa")
            return redirect('work_statuses')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def work_status_add(request):
    """
    Handles adding status to database while checking if the user is authenticated and has permission to add work status.
    Function also checks if there already exists work status by the same name.
    """
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
            return render(request, 'professors/work_statuses/work_status_add.html')
        else:
            messages.error(request, "Nemate ovlaštenje za dodavanje radnog statusa")
            return redirect('work_statuses')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def work_status_update(request, status_id):
    """
    Updating work status only checks if user has permission to update status by it's id.
    If request user doesn't have permission to update status, system redirects user to all statuses and shows
    corresponding message.
    """
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
    """
    Deleting work status checks if request user has permission to delete, and if not, system redirects user to
    page for viewing that status and shows corresponding message.
    """
    status = get_object_or_404(models.WorkStatus, pk=status_id)
    if request.user.has_perm("professors.delete_workstatus"):
        if request.method == 'POST':
            status.delete()
            messages.success(request, "Uspješno obrisan status")
            return redirect('work_statuses')
    else:
        messages.error(request, "Nemate ovlaštenje za brisanje radnog statusa")
        return redirect('single_work_status', status_id=status_id)


def academic_titles(request):
    """
    Handle getting all academic titles objects with pagination.
    If user is not authenticated, system redirects to login page with corresponding message.
    """
    if request.user.is_authenticated:
        titles = models.AcademicTitle.objects.all().order_by('id')
        paginator = Paginator(titles, 10)
        page = request.GET.get('page')

        try:
            paged_titles = paginator.get_page(page)
        except PageNotAnInteger:
            paged_titles = paginator.page(1)
        except EmptyPage:
            paged_titles = paginator.page(paginator.num_pages)

        context = {
            'titles': paged_titles,
        }

        return render(request, "professors/academic_titles/academic_titles.html", context)
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def single_academic_title(request, title_id):
    """
    Handles listing single academic title for given title id.
    Function checks if user is authenticated and has permission to view title. If user is not authenticated
    or doesn't have permission to view title, system redirects request user to other pages with corresponding messages.
    """
    if request.user.is_authenticated:
        if request.user.has_perm("professors.view_academictitle"):
            title = get_object_or_404(models.AcademicTitle, pk=title_id)
            context = {
                'title': title,
            }
            return render(request, "professors/academic_titles/single_academic_title.html", context)
        else:
            messages.error(request, "Niste ovlašteni za pregled akademske titule")
            return redirect('academic_titles')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def academic_title_add(request):
    """
    Handles adding academic title to database while checking if the user is authenticated and has permission to add
    academic title.
    Function also checks if there already exists academic title by the same name.
    """
    if request.user.is_authenticated:
        if request.user.has_perm("professors.add_academictitle"):
            if request.method == 'POST':
                name = request.POST['Name']
                if models.AcademicTitle.objects.filter(name=name).exists():
                    messages.error(request, "Titula već postoji u bazi")
                    return redirect('academic_title_add')
                else:
                    title = models.AcademicTitle(name=name)
                    title.save()
                    messages.success(request, "Uspješno dodana akademska titula")
                    return redirect('academic_titles')
            return render(request, 'professors/academic_titles/academic_title_add.html')
        else:
            messages.error(request, "Nemate ovlaštenje za dodavanje akademske titule")
            return redirect('academic_titles')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def academic_title_update(request, title_id):
    """
    Updating academic title only checks if user has permission to update academic title by it's id.
    If request user doesn't have permission to update, system redirects user to all academic titles and shows
    corresponding message.
    """
    title = get_object_or_404(models.AcademicTitle, pk=title_id)
    if request.user.has_perm("professors.change_academictitle"):
        if request.method == 'POST':
            title.name = request.POST.get("Name")
            title.save()
            messages.success(request, "Uspješna izmjena")
            return redirect('single_academic_title', title_id=title_id)
    else:
        messages.error(request, "Nemate ovlaštenje za izmjenu akademske titule")
        return redirect('academic_titles')


def academic_title_delete(request, title_id):
    """
    Deleting academic title checks if request user has permission to delete, and if not, system redirects user to
    page for viewing that title and shows corresponding message.
    """
    title = get_object_or_404(models.AcademicTitle, pk=title_id)
    if request.user.has_perm("professors.delete_academictitle"):
        if request.method == 'POST':
            title.delete()
            messages.success(request, "Uspješno obrisana akademska titula")
            return redirect('academic_titles')
    else:
        messages.error(request, "Nemate ovlaštenje za brisanje akademske titule")
        return redirect('single_academic_title', title_id=title_id)


def engagements(request):
    """
    Handle getting all engagements objects with pagination.
    If user is not authenticated, system redirects to login page with corresponding message.
    """
    if request.user.is_authenticated:
        all_engagements = models.Engagement.objects.all().order_by('id')
        paginator = Paginator(all_engagements, 10)
        page = request.GET.get('page')

        try:
            paged_engagements = paginator.get_page(page)
        except PageNotAnInteger:
            paged_engagements = paginator.page(1)
        except EmptyPage:
            paged_engagements = paginator.page(paginator.num_pages)

        context = {
            'engagements': paged_engagements,
        }

        return render(request, "professors/engagements/engagements.html", context)
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def single_engagement(request, engagement_id):
    """
    Handles listing single engagement for given title id.
    Function checks if user is authenticated and has permission to view engagement. If user is not authenticated
    or doesn't have permission to view, system redirects request user to other pages with corresponding messages.
    """
    if request.user.is_authenticated:
        if request.user.has_perm("professors.view_engagement"):
            engagement = get_object_or_404(models.Engagement, pk=engagement_id)
            context = {
                'engagement': engagement,
            }
            return render(request, "professors/engagements/single_engagement.html", context)
        else:
            messages.error(request, "Niste ovlašteni za pregled angažovanja")
            return redirect('engagements')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def engagement_add(request):
    """
    Handles adding new engagement to database while checking if the user is authenticated and has permission to add
    engagement.
    Function also checks if there already exists engagement by the same name.
    """
    if request.user.is_authenticated:
        if request.user.has_perm("professors.add_engagement"):
            if request.method == 'POST':
                name = request.POST['Name']
                if models.Engagement.objects.filter(name=name).exists():
                    messages.error(request, "Angazovanje već postoji u bazi")
                    return redirect('engagement_add')
                else:
                    engagement = models.Engagement(name=name)
                    engagement.save()
                    messages.success(request, "Uspješno dodano angazovanje")
                    return redirect('engagements')
            return render(request, 'professors/engagements/engagement_add.html')
        else:
            messages.error(request, "Nemate ovlaštenje za dodavanje angazovanja")
            return redirect('engagements')
    else:
        messages.error(request, "Prijavite se na sistem")
        return redirect('user_login')


def engagement_update(request, engagement_id):
    """
    Updating engagement only checks if user has permission to update engagement by it's id.
    If request user doesn't have permission to update, system redirects user to all engagements and shows
    corresponding message.
    """
    engagement = get_object_or_404(models.Engagement, pk=engagement_id)
    if request.user.has_perm("professors.change_engagement"):
        if request.method == 'POST':
            engagement.name = request.POST.get("Name")
            engagement.save()
            messages.success(request, "Uspješna izmjena")
            return redirect('single_engagement', engagement_id=engagement_id)
    else:
        messages.error(request, "Nemate ovlaštenje za izmjenu radnog statusa")
        return redirect("work_statuses")


def engagement_delete(request, engagement_id):
    """
    Deleting engagement checks if request user has permission to delete, and if not, system redirects user to
    page for viewing that engagement and shows corresponding message.
    """
    engagement = get_object_or_404(models.Engagement, pk=engagement_id)
    if request.user.has_perm("professors.delete_engagement"):
        if request.method == 'POST':
            engagement.delete()
            messages.success(request, "Uspješno obrisano angazovanje")
            return redirect('engagements')
    else:
        messages.error(request, "Nemate ovlaštenje za brisanje angazovanja")
        return redirect('single_engagement', engagement_id=engagement_id)
