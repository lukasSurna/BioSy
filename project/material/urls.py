from django.urls import path
from . import views

app_name = "material"

urlpatterns = [
    path("", views.index, name="index"),
    #Groups main view
    path("groups/", views.groups, name="groups"),
    #Add new group
    path("groups/add/", views.add_group, name="add_group"),
    #Edit group
    path("groups/edit/<int:id>", views.edit_group, name="edit_group"),
    #Delete group
    path("groups/delete/<int:id>", views.delete_group, name="delete_group"),

    #Supplier view
    path("suppliers/", views.suppliers, name="suppliers"),
    #Supplier detail
    path("suppliers/<int:id>", views.supplier_detail, name="supplier_detail"),
    #Add new supplier
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    #Edit supplier
    path("suppliers/edit/<int:id>", views.edit_supplier, name="edit_supplier"),
    #Delete supplier
    path("suppliers/delete/<int:id>", views.delete_supplier, name="delete_supplier"),

    #Material view
    path("materials/", views.materials, name="materials"),
    #Add new material
    path("materials/add/", views.add_material, name="add_material"),
]