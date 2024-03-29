from django.db import models
from django.db.models import SET_NULL
from kadedit.models import TimeModelMixin
from subjects.models import Subject
from django.utils.translation import ugettext_lazy as _


class WorkStatus(models.Model):
    name = models.CharField(_('work status'), max_length=65, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("work status")
        verbose_name_plural = _("work statuses")


class Engagement(models.Model):
    name = models.CharField(_('calling'), max_length=65, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("calling")
        verbose_name_plural = _("engagements")


class AcademicTitle(models.Model):
    name = models.CharField(_('academic title'), max_length=65, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("academic title")
        verbose_name_plural = _("academic titles")


class Calling(models.Model):
    name = models.CharField(_('calling'), max_length=65, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('calling')
        verbose_name_plural = _('callings')


class Professor(TimeModelMixin):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=80)
    birthdate = models.DateField(_('birthdate'), blank=True, null=True)
    dissertation = models.CharField(_("dissertation"), max_length=200, blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    work_status = models.ForeignKey(WorkStatus, blank=True, null=True, on_delete=SET_NULL,
                                    verbose_name=_("work status"))
    # calling = models.ForeignKey(Engagement, blank=True, null=True, on_delete=SET_NULL,
    #                                verbose_name=_("calling"))
    calling = models.ForeignKey(Calling, blank=True, null=True, on_delete=SET_NULL,
                                verbose_name=_("calling"))
    academic_title = models.ForeignKey(AcademicTitle, blank=True, null=True, on_delete=SET_NULL,
                                       verbose_name=_("academic title"))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _("professor")
        verbose_name_plural = _("professors")


class XProfessorSubject(models.Model):
    professor = models.ForeignKey(Professor, null=True, on_delete=SET_NULL, verbose_name=_("professor"))
    subject = models.ForeignKey(Subject, null=True, on_delete=SET_NULL, verbose_name=_("subject"))
    practice = models.BooleanField(_("practice"), default=False, blank=True)

    def __str__(self):
        return f'{self.professor}: {self.subject}'

    class Meta:
        verbose_name = _("professor subject information")
        verbose_name_plural = _("professor subjects information")
        db_table = 'x_professor_subject'
