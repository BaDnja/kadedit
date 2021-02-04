from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models


@login_required
def view_multiple_objects(request, queryset, template):
    """Handle getting and displaying multiple objects"""
    query = queryset

    paginator = Paginator(query, 15)
    page = request.GET.get('page')

    try:
        paged_query = paginator.get_page(page)
    except PageNotAnInteger:
        paged_query = paginator.page(1)
    except EmptyPage:
        paged_query = paginator.page(paginator.num_pages)

    context = {
        'obj_list': paged_query,
    }
    return render(request, template, context)


@login_required
def view_single_object(request, query, template):
    """Handle getting single object page"""
    obj = query
    context = {
        'object': obj,
    }

    return render(request, template, context)


@login_required
def add_single_object(request, model, template, error_redirect, success_redirect):
    """
    Function adds new object to a database with only one field: name.
    Handles adding new object to database while checking if the user is authenticated.
    Function also checks if there already exists object with the same name.

    query: checks if the particular object already exists.
    model: which model gets checked of form submit.
    template: returns template for rendering.
    error_redirect: redirects to error view if object exists.
    success_redirect: redirects to success view after saving new object.
    """
    if request.method == 'POST':
        name = request.POST['Name']

        if model.objects.filter(name=name).exists():
            messages.error(request, "Objekat već postoji")
            return redirect(error_redirect)
        else:
            new_object = model(name=name)
            new_object.save()
            messages.success(request, "Objekat uspješno dodan")
            return redirect(success_redirect)
    return render(request, template)


@login_required
def update_single_object(request, object_to_update, object_id, success_redirect):
    """
    Updating single object checks if user is logged in,
    and function that calls this one, checks is user has permission to update object by it's id.
    If request user doesn't have permission to update object, system redirects user to all objects of that view and shows
    corresponding message.
    """
    obj = object_to_update
    if request.method == 'POST':
        obj.name = request.POST.get("Name")
        obj.save()
        messages.success(request, "Uspješna izmjena")
        return redirect(success_redirect, object_id)


def professors(request):
    """Handle getting main page for professors"""
    queryset = models.Professor.objects.filter(active=True).order_by('-id')
    template = 'professors/professors/dashboard-professors.html'
    return view_multiple_objects(request, queryset, template)


@permission_required('professors.view_professor', raise_exception=True)
def professor(request, professor_id):
    """Handle getting single page for professor"""
    obj = get_object_or_404(models.Professor, pk=professor_id)
    template = 'professors/professors/professor.html'
    return view_single_object(request, obj, template)


def work_statuses(request):
    """
    Handles getting page for listing all work statuses in the system.
    Function check if request user is authenticated. If not, it redirects the user to the login page.
    If user is authenticated, it creates pagination and lists all work statuses for that pagination page.
    """
    queryset = models.WorkStatus.objects.all().order_by('id')
    template = 'professors/work_statuses/work_statuses.html'
    return view_multiple_objects(request, queryset, template)


@permission_required('professors.view_workstatus', raise_exception=True)
def single_work_status(request, status_id):
    """
    Handles listing single work status for given status id.
    Function checks if user is authenticated and has permission to view status. If user is not authenticated
    or doesn't have permission to view status, system redirects request user to other pages with corresponding messages.
    """
    obj = get_object_or_404(models.WorkStatus, pk=status_id)
    template = 'professors/work_statuses/single_work_status.html'
    return view_single_object(request, obj, template)


@permission_required('professors.add_workstatus', raise_exception=True)
def work_status_add(request):
    model = models.WorkStatus
    template = 'professors/work_statuses/work_status_add.html'
    err_redirect = 'work_status_add'
    succ_redirect = 'work_statuses'
    return add_single_object(request, model, template, err_redirect, succ_redirect)


@permission_required('professors.change_workstatus', raise_exception=True)
def work_status_update(request, status_id):
    obj = get_object_or_404(models.WorkStatus, pk=status_id)
    obj_id = status_id
    succ_redirect = 'single_work_status'
    return update_single_object(request, obj, obj_id, succ_redirect)


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
    queryset = models.AcademicTitle.objects.all().order_by('id')
    template = 'professors/academic_titles/academic_titles.html'
    return view_multiple_objects(request, queryset, template)


@permission_required('professors.view_academictitle', raise_exception=True)
def single_academic_title(request, title_id):
    """
    Handles listing single academic title for given title id.
    Function checks if user is authenticated and has permission to view title. If user is not authenticated
    or doesn't have permission to view title, system redirects request user to other pages with corresponding messages.
    """
    obj = get_object_or_404(models.AcademicTitle, pk=title_id)
    template = 'professors/academic_titles/single_academic_title.html'
    return view_single_object(request, obj, template)


@permission_required('professors.add_academictitle', raise_exception=True)
def academic_title_add(request):
    model = models.AcademicTitle
    template = 'professors/academic_titles/academic_title_add.html'
    err_redirect = 'academic_title_add'
    succ_redirect = 'academic_titles'
    return add_single_object(request, model, template, err_redirect, succ_redirect)


@permission_required('professors.change_academictitle', raise_exception=True)
def academic_title_update(request, title_id):
    obj = get_object_or_404(models.AcademicTitle, pk=title_id)
    object_id = title_id
    succ_redirect = 'single_academic_title'
    return update_single_object(request, obj, object_id, succ_redirect)


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
    queryset = models.Engagement.objects.all().order_by('id')
    template = 'professors/engagements/engagements.html'
    return view_multiple_objects(request, queryset, template)


@permission_required('professors.view_engagement', raise_exception=True)
def single_engagement(request, engagement_id):
    """
    Handles listing single engagement for given title id.
    Function checks if user is authenticated and has permission to view engagement. If user is not authenticated
    or doesn't have permission to view, system redirects request user to other pages with corresponding messages.
    """
    obj = get_object_or_404(models.Engagement, pk=engagement_id)
    template = 'professors/engagements/single_engagement.html'
    return view_single_object(request, obj, template)


@permission_required('professors.add_engagement', raise_exception=True)
def engagement_add(request):
    model = models.Engagement
    template = 'professors/engagements/engagement_add.html'
    err_redirect = 'engagement_add'
    succ_redirect = 'engagements'
    return add_single_object(request, model, template, err_redirect, succ_redirect)


@permission_required('professors.change_engagement', raise_exception=True)
def engagement_update(request, engagement_id):
    obj = get_object_or_404(models.Engagement, pk=engagement_id)
    object_id = engagement_id
    succ_redirect = 'single_engagement'
    return update_single_object(request, obj, object_id, succ_redirect)


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
