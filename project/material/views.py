from django.shortcuts import render, redirect
from slugify import slugify
from django.contrib import messages
from . import models
from . import forms


def index(request):
    return render(request, "material/index.html")

#Groups views
def groups(request):
    groups = models.Group.objects.all()
    context = {"groups": groups}
    return render(request, "material/groups.html", context)

def add_group(request): #Need to fix Warning Error (to show non-unique slug warning) 
    non_unique_slug_warning = None

    if request.method == "POST":
        form = forms.GroupForm(request.POST)
        if form.is_valid():
            # Extract name from the form
            group_name = form.cleaned_data["name"]
            # Generate a unique slug using the name
            slug = slugify(group_name)
            # Check if a group with the generated slug already exists
            if models.Group.objects.filter(slug=slug).exists():
                # Handle non-unique slug
                non_unique_slug_warning = "Warning: The provided group name results in a non-unique slug. Please choose a different name."
            else:
                # Create a new group instance with the correct slug
                new_group = form.save(commit=False)
                new_group.slug = slug
                new_group.save()
                return redirect("material:groups")
    else:
        form = forms.GroupForm()

    return render(request, "material/add_group.html", {"form": form, "non_unique_slug_warning": non_unique_slug_warning})
    
def edit_group(request, id):
    group = models.Group.objects.get(id=id)
    if request.method == "POST":
        form = forms.GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("material:groups")
    else:
        form = forms.GroupForm(instance=group)
    return render(request, "material/edit_group.html", {"form": form})

def delete_group(request, id):
    group = models.Group.objects.get(id=id)
    group.delete()
    return redirect("material:groups")

#END OF GROUPS view

#Suppliers view
def suppliers(request):
    suppliers = models.Supplier.objects.all()
    context = {"suppliers": suppliers}
    return render(request, "material/suppliers.html", context)

def supplier_detail(request, id):
    supplier = models.Supplier.objects.get(id=id)
    materials = models.Material.objects.filter(supplier=supplier)
    context = {"supplier": supplier, "materials": materials}
    return render(request, "material/supplier_detail.html", context)

def add_supplier(request):
    if request.method == "POST":
        form = forms.SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:suppliers")
    else:
        form = forms.SupplierForm()
    return render(request, "material/add_supplier.html", {"form": form})

def edit_supplier(request, id):
    supplier = models.Supplier.objects.get(id=id)

    if request.method == 'POST':
        form = forms.SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, f'{supplier} edited successfully!')
            return redirect('material:suppliers')  # Redirect to the suppliers list with success message
    else:
        form = forms.SupplierForm(instance=supplier)

    return render(request, 'material/edit_supplier.html', {'supplier': supplier, 'form': form})
def delete_supplier(request, id):
    supplier = models.Supplier.objects.get(id=id)
    supplier.delete()
    return redirect("material:suppliers")

#END OF SUPPLIERS view

#Materials view
def materials(request):
    materials = models.Material.objects.all()
    context = {"materials": materials}
    return render(request, "material/materials.html", context)

def add_material(request):
    if request.method == "POST":
        form = forms.MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("material:materials")
    else:
        form = forms.MaterialForm()
    return render(request, "material/add_material.html", {"form": form})