from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeModelMixin(models.Model):
    """Mixin that handles creation, modification dates"""
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DeletionModelMixin(models.Model):
    """Mixin that handles deletion state and deletion date"""
    deleted = models.BooleanField(verbose_name=_("deleted"), default=False)
    deletion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
