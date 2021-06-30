from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.models.RawMaterial import RawMaterial
from productionplanning.forms.RawMaterialForm import RawMaterialForm, ViewRawMaterialForm
from productionplanning.filters.RawMaterialFilter import RawMaterialFilter
from .CustomFunction import get_db_for_date
from django.contrib import messages
from datetime import *

list_raw_material_props = {
    "title": "Raw Material",
}

post_raw_material_props = {
    "title": "New Raw Material",
}

views_raw_material_props = {
    "title": "View Raw Material",
}

update_raw_material_props = {
    "title": "Update Raw Material",
    "btn_name": 'Update'
}

copy_raw_material_props = {
    "title": "Copy Raw Material",
    "btn_name": 'Copy'
}


def ListRawMaterial(request):
    print(get_db_for_date(db_name=RawMaterial))
    list_raw_material_props.update({"lengths": len(RawMaterial.objects.all())})
    allRawMaterial = RawMaterial.objects.all()
    filter = RawMaterialFilter()
    list_raw_material_props['RawMaterials'] = allRawMaterial
    list_raw_material_props['filters'] = filter

    return render(request, 'PP/rawmaterial/list.html', context=list_raw_material_props)


def FilterRawMaterial(request):
    if request.method == 'POST':
        filter = RawMaterialFilter(request.POST, queryset=RawMaterial.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'RawMaterials': list(filter.qs.values()),
                    'mass': 'success',
                }, status=200)
            else:
                return JsonResponse({
                    'mass': 'error',
                }, status=200)
        else:
            return JsonResponse({
                'mass': 'error',
            })
    else:
        return JsonResponse({
            'mass': 'error',
        })


def PostRawMaterial(request):
    if request.method == "POST":
        RawMaterialForms = RawMaterialForm(request.POST)
        if RawMaterialForms.is_valid():
            RawMaterialForms.save()
            messages.success(request, 'Raw Material Created Successfully.')
            return redirect('/productionplanning/raw-material/')
        else:
            messages.error(request, 'Raw Material Not Created Successfully.')
            return redirect('/productionplanning/raw-material/')
    else:
        RawMaterialForms = RawMaterialForm()
        post_raw_material_props["forms"] = RawMaterialForms
        return render(request, 'PP/rawmaterial/forms.html', context=post_raw_material_props)


def ViewRawMaterial(request, id):
    instancrs = RawMaterial.objects.get(id=id)
    views_raw_material_props['id'] = id
    views_raw_material_props['forms'] = ViewRawMaterialForm(instance=instancrs)
    return render(request, 'PP/rawmaterial/views.html', context=views_raw_material_props)


def UpdateRawMaterial(request, id):
    instancrs = RawMaterial.objects.get(id=id)
    update_raw_material_props['id'] = id
    if request.method == "POST":
        RawMaterialForms = RawMaterialForm(request.POST, instance=instancrs)
        if RawMaterialForms.has_changed():
            if RawMaterialForms.is_valid():
                RawMaterialForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/raw-material/')
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/raw-material/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/raw-material/')
    else:
        update_raw_material_props['forms'] = RawMaterialForm(instance=instancrs)
        return render(request, 'PP/rawmaterial/update.html', context=update_raw_material_props)


def CopyRawMaterial(request, id):
    instancrs = RawMaterial.objects.get(id=id)
    if request.method == "POST":
        RawMaterialForms = RawMaterialForm(request.POST, instance=instancrs)
        if RawMaterialForms.has_changed():
            RawMaterialForms = RawMaterialForm(data=request.POST)
            if RawMaterialForms.is_valid():
                forms = RawMaterialForms.save()
                messages.success(request, '{} to {} Copy Successfully.'.format(id, forms.id))
                return redirect('/productionplanning/raw-material/')
            else:
                messages.error(request, '{} Copy Is Not Successful.'.format(id))
                return redirect('/productionplanning/raw-material/')
        else:
            messages.error(request, '{} Value Is Not Change.'.format(id))
            return redirect('/productionplanning/raw-material/')
    else:
        copy_raw_material_props['id'] = id
        copy_raw_material_props['forms'] = RawMaterialForm(instance=instancrs)
        return render(request, 'PP/rawmaterial/update.html', context=copy_raw_material_props)


def DeleteRawMaterial(request, id):
    Material = RawMaterial.objects.get(id=id)
    Material.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/raw-material/')
