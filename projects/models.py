from django.db import models
from django.utils.translation import gettext_lazy as _


class Projects(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.name
