from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProfessorsConfig(AppConfig):
    name = 'professors'
    verbose_name = _("professors")
