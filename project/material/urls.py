from django.urls import path
from . import views

app_name = "material"

urlpatterns = [
    path("", views.index, name="index"),
    #Groups main view
    path("groups/", views.groups, name="groups"),
]