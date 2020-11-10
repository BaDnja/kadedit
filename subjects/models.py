from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import ugettext_lazy as _


class Faculty(models.Model):
    name = models.CharField(_('faculty'), max_length=70, unique=True)
    short = models.CharField(_('short'), max_length=10, unique=True)

    def __str__(self):
        return f'{self.short}'

    class Meta:
        ordering = ['short']
        verbose_name = _("faculty")
        verbose_name_plural = _("faculties")


class StudyCycle(models.Model):
    name = models.CharField(_('study cycle'), max_length=70, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("study cycle")
        verbose_name_plural = _("study cycles")


class SubjectType(models.Model):
    name = models.CharField(_('subject type'), max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("subject type")
        verbose_name_plural = _("subject types")


class StudyProgram(models.Model):
    name = models.CharField(_('study program'), max_length=100)
    short = models.CharField(_("short"), max_length=10, unique=True)
    study_cycle = models.ForeignKey(StudyCycle, null=True, on_delete=SET_NULL, verbose_name=_("study cycle"))
    faculty = models.ForeignKey(Faculty, null=True, on_delete=SET_NULL, verbose_name=_("faculty"))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _("study program")
        verbose_name_plural = _("study programs")


class Semester(models.Model):
    name = models.CharField(_('semester'), max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("semester")
        verbose_name_plural = _("semesters")


class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    name = models.CharField(_('subject'), max_length=120, unique=True)
    semester = models.ManyToManyField(Semester)
    ects = models.IntegerField(_("ects"), blank=False, null=False)
    subject_type = models.ForeignKey(SubjectType, null=True, on_delete=SET_NULL, verbose_name=_("subject type"))
    study_program = models.ManyToManyField(StudyProgram)

    def __str__(self):
        return f'{self.name}'

    def semesters(self):
        return ",\n".join([str(s.id) for s in self.semester.all()])
    semesters.short_description = _("semesters")

    def study_programs(self):
        return ",\n".join([s.short for s in self.study_program.all()])
    study_programs.short_description = _("study programs")

    class Meta:
        ordering = ['name']
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")
