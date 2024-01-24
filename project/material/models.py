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
    

class Supplier(models.Model):
    supplier = models.CharField(_("Supplier"), max_length=100, unique=True)
    country = models.CharField(_("Country"), max_length=100)
    contact_person = models.CharField(_("Contact Person"), max_length=100, default=None)
    email = models.EmailField(_("Email"), max_length=70, default=None)
    phone = models.CharField(_("Phone"), max_length=20, default=None)

    class Meta:
        verbose_name = _("supplier")
        verbose_name_plural = _("suppliers")
        ordering = ["supplier"]

    def __str__(self):
        return self.supplier
    

class Material(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    material_number = models.CharField(_("Material Number"), max_length=15, unique=True, default=None)
    material_id = models.CharField(_("Material ID"), max_length=15,primary_key=True, unique=True, default=None)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("material")
        verbose_name_plural = _("materials")
        ordering = ["name"]

    def __str__(self):
        return self.name
