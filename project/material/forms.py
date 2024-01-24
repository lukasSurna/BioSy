from django import forms
from . import models

class GroupForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = ["name"]


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = ["supplier", "country", "contact_person", "email", "phone"]


class MaterialForm(forms.ModelForm):

    class Meta:
        model = models.Material
        fields = ["name", "material_number", "material_id", "group", "supplier"]