from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("material:group_detail", kwargs={"slug": self.slug})
    
    def get_url(self):
        return reverse("material:group_detail", kwargs={"slug": self.slug})


