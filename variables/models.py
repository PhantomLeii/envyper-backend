from django.db import models
from django.utils.translation import gettext_lazy as _


class Variable(models.Model):
    key = models.CharField(_("Key"), max_length=150)
    value = models.TextField(_("Value"))
    project = models.ForeignKey(
        "projects.Projects", verbose_name=_("Project"), on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.key

    def get_value(self):
        pass

    def set_value(self, raw_value):
        pass
