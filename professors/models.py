from django.db import models
from django.db.models import SET_NULL, CASCADE
from subjects.models import Subject
from django.utils.translation import ugettext_lazy as _


class Professor(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=80)
    birthdate = models.DateField(_('birthdate'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class WorkStatus(models.Model):
    name = models.CharField(_('work status'), max_length=35, unique=True)


class Engagement(models.Model):
    name = models.CharField(_('engagement'), max_length=50, unique=True)


class AcademicTitle(models.Model):
    name = models.CharField(_('academic title'), max_length=65, unique=True)


class ProfessorInfo(models.Model):
    dissertation = models.CharField(max_length=200, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=CASCADE)
    work_status = models.ForeignKey(WorkStatus, null=True, on_delete=SET_NULL)
    engagement = models.ForeignKey(Engagement, null=True, on_delete=SET_NULL)
    academic_title = models.ForeignKey(AcademicTitle, null=True, on_delete=SET_NULL)


class XProfessorSubject(models.Model):
    professor = models.ForeignKey(Professor, null=True, on_delete=SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=SET_NULL)
    practice = models.BooleanField(default=False, blank=True)

    class Meta:
        db_table = 'x_professor_subject'
