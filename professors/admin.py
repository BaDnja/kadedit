from django.contrib import admin
from .models import *


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birthdate", "engagement", "academic_title", "work_status")
    list_per_page = 25
    list_display_links = ("first_name", "last_name", "academic_title")
    search_fields = ("first_name", "last_name", "engagement__name", "academic_title__name", "work_status__name")
    list_filter = ("engagement", "work_status", "academic_title")
    list_editable = ("engagement", "work_status")
    exclude = ['deletion_date']


@admin.register(WorkStatus)
class WorkStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 15


@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 10


@admin.register(AcademicTitle)
class AcademicTitleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 10
    search_fields = ("name",)


@admin.register(XProfessorSubject)
class XProfessorSubjectAdmin(admin.ModelAdmin):
    list_display = ("professor", "subject", "practice")
    list_per_page = 30
    list_display_links = ("professor", "subject")
    search_fields = ("professor__first_name", "professor__last_name", "subject__name")
    list_editable = ("practice",)
    list_filter = ("practice",)
