from django.shortcuts import render
from . import models

def index(request):
    return render(request, "material/index.html")

def groups(request):
    groups = models.Group.objects.all()
    context = {"groups": groups}
    return render(request, "material/groups.html", context)