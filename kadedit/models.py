# from django.contrib.auth.models import User
from django.db import models
# from django.db.models import SET_NULL
from django.utils.translation import ugettext_lazy as _


class TimeModelMixin(models.Model):
    """Mixin that handles model activity dates"""
    creation_date = models.DateTimeField(verbose_name=_("datum kreiranja"), auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name=_("datum izmjene"), auto_now=True)
    #deactivation_date = models.DateTimeField(verbose_name=_("datum deaktivacije"), blank=True, null=True)

    class Meta:
        abstract = True

#
# class ActivityModelMixin(models.Model):
#     """Mixin that handles model activity"""
#     created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
#     last_modified_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
#     active = models.BooleanField(verbose_name=_("active"), default=True)
#     activated_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
#     deactivated_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
#
#     class Meta:
#         abstract = True
