from django.db import models
from django.db.models import SET_NULL, CASCADE
from django.utils.translation import ugettext_lazy as _


class Faculty(models.Model):
    name = models.CharField(_('faculty'), max_length=70, unique=True)
    short = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.short}'

    class Meta:
        ordering = ['short']


class StudyCycle(models.Model):
    name = models.CharField(_('study cycle'), max_length=70, unique=True)


class SubjectType(models.Model):
    name = models.CharField(_('subject type'), max_length=30, unique=True)


class StudyProgram(models.Model):
    name = models.CharField(_('study program'), max_length=100)
    short = models.CharField(max_length=10, unique=True)
    study_cycle = models.ForeignKey(StudyCycle, null=True, on_delete=SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=SET_NULL)

    def __str__(self):
        return

    class Meta:
        ordering = ['name']


class Semester(models.Model):
    name = models.CharField(_('semester'), max_length=100, unique=True)


class Ects(models.Model):
    ects = models.IntegerField(_('european credit transfer system'), unique=True, default=5)
    name = models.CharField(max_length=25, unique=True)


class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    name = models.CharField(_('subject'), max_length=120, unique=True)
    semester = models.ManyToManyField(Semester)
    ects = models.ManyToManyField(Ects)
    subject_type = models.ForeignKey(SubjectType, null=True, on_delete=SET_NULL)
    study_program = models.ForeignKey(StudyProgram, null=True, on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
