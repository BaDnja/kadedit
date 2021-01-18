from django.contrib import admin
from .models import *


@admin.register(Faculty)
class FacultiesAdmin(admin.ModelAdmin):
    list_display = ("name", "short")


@admin.register(StudyCycle)
class StudyCycleAdmin(admin.ModelAdmin):
    pass


@admin.register(SubjectType)
class SubjectTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(StudyProgram)
class StudyProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "short", "study_cycle", "faculty")
    list_filter = ("name", "faculty")
    search_fields = ("name", "short", "faculty__short")
    list_editable = ("faculty",)
    list_per_page = 25


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "ects", "subject_type", "semesters", "study_programs")
