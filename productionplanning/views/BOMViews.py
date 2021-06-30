from django.shortcuts import render, redirect

from productionplanning.filters.BOMFilter import BOMFilter
from productionplanning.models.BOM import BOM
from productionplanning.forms.BOMForm import BOMForm, BomAndRowMaterialForm, BomAndRowMaterialForm2, \
    BOMForm2, BomAndRowMaterialForm3
from productionplanning.models.RawMaterial import RawMaterial
from productionplanning.models.BomAndRawMaterial import BomAndRowMaterial
from django.http import JsonResponse
from django.contrib import messages
from django.forms.models import modelformset_factory

list_BOM_props = {
    "title": "BOM",
}

post_BOM_props = {
    "title": "New BOM",
}

views_BOM_props = {
    "title": "View BOM",
}

update_BOM_props = {
    "title": "Update BOM",
    "btn_name": 'Update'
}

copy_BOM_props = {
    "title": "Copy BOM",
    "btn_name": 'Copy'
}


def ListBOM(request):
    list_BOM_props['products'] = BOM.objects.all()
    list_BOM_props['filters'] = BOMFilter()
    return render(request, 'PP/bom/list.html', context=list_BOM_props)


def FilterBOM(request):
    if request.method == 'POST':
        filter = BOMFilter(request.POST, queryset=BOM.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'BOMs': list(filter.qs.values()),
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


def PostBOM(request):
    if request.method == "POST":
        boms = BOMForm(data=request.POST)
        if boms.is_valid():
            bom = boms.save()
            messages.success(request, "Bom Created Successfully")
            return redirect('/productionplanning/add-raw-in-bom/' + bom.id)
        else:
            messages.error(request, "Bom Not Created Successfully")
            return redirect('/productionplanning/bom/')
    else:
        BOMForms = BOMForm()
        post_BOM_props["forms"] = BOMForms
        return render(request, 'PP/bom/forms.html', context=post_BOM_props)


def RawInBOM(request, id):
    if request.method == "POST":
        bom_raw = BomAndRowMaterialForm(request.POST)
        if bom_raw.is_valid():
            bom_raw = bom_raw.save(commit=False)
            bom_raw.bom = BOM.objects.get(id=id)
            bom_raw.save()
            messages.success(request, "Add Raw Material Successfully")
            return redirect('/productionplanning/add-raw-in-bom/' + id)
        else:
            messages.error(request, "Raw Material Not Add Successfully")
            return redirect('/productionplanning/add-raw-in-bom/' + id)
    else:
        bom = BOM.objects.get(id=id)
        post_BOM_props['id'] = bom.id
        post_BOM_props['bom'] = bom
        post_BOM_props['RowMaterial'] = BomAndRowMaterial.objects.filter(bom_id=id)
        post_BOM_props['id'] = id
        post_BOM_props['forms'] = BOMForm(instance=bom)
        post_BOM_props["BomAndRowMaterialForm"] = BomAndRowMaterialForm()
        if request.is_ajax():
            raw_id = request.GET.get('raw_id')
            raw = RawMaterial.objects.filter(id=raw_id).values()
            return JsonResponse({'RawMaterial': list(raw)})
        return render(request, 'PP/bom/raw_in_bom.html', context=post_BOM_props)


def FinishedRawInBOM(request, id):
    if request.method == "POST":
        bom_raw = BomAndRowMaterialForm(request.POST)
        if bom_raw.is_valid():
            bom_raw = bom_raw.save(commit=False)
            bom_raw.bom = BOM.objects.get(id=id)
            bom_raw.save()
            messages.success(request, "Add Raw Material Successfully")
            return redirect('/productionplanning/bom/')
        else:
            messages.error(request, "Raw Material Not Add Successfully")
            return redirect('/productionplanning/bom/')


def ViewBOM(request, id):
    views_BOM_props['id'] = id
    views_BOM_props['Bom'] = BOM.objects.get(id=id)
    views_BOM_props['BomAndRowMaterial'] = BomAndRowMaterial.objects.filter(bom=id)
    return render(request, 'PP/bom/views.html', context=views_BOM_props)


def UpdateBOM(request, id):
    instancrs = BOM.objects.get(id=id)
    bom_raw = BomAndRowMaterial.objects.filter(bom_id=id)
    update_BOM_props['id'] = id
    bnr = BomAndRowMaterial.objects.filter(bom=id)
    RawBomFormSet = modelformset_factory(BomAndRowMaterial, form=BomAndRowMaterialForm2, extra=0)
    update_BOM_props['formset'] = RawBomFormSet(queryset=bnr)
    update_BOM_props["BomAndRowMaterialForm"] = BomAndRowMaterialForm3()
    if request.method == "POST":
        bom = BOM.objects.get(id=id)
        Bom = BOMForm(request.POST, instance=bom)
        bom_raw = BomAndRowMaterialForm3(request.POST)

        if Bom.has_changed():
            if Bom.is_valid():
                Bom.save()
                messages.success(request, "{} Update Successfully.".format(id))
                return redirect('/productionplanning/update-bom/' + id)
            elif bom_raw.is_valid():
                bom_raw = bom_raw.save(commit=False)
                bom_raw.bom = BOM.objects.get(id=id)
                bom_raw.save()
                messages.success(request, "Add Raw Material Successfully")
                return redirect('/productionplanning/update-bom/' + id)
            else:
                messages.error(request, "{} Not Update Successfully.".format(id))
                return redirect('/productionplanning/update-bom/' + id)
        else:
            messages.error(request, "{} Value Not Change.".format(id))
            return redirect('/productionplanning/update-bom/' + id)

    else:
        update_BOM_props['bom_raw'] = bom_raw
        update_BOM_props['forms'] = BOMForm2(instance=instancrs)
        if request.is_ajax():
            raw_id = request.GET.get('raw_id')
            raw = RawMaterial.objects.filter(id=raw_id).values()
            return JsonResponse({'RawMaterial': list(raw)})
        return render(request, 'PP/bom/update.html', context=update_BOM_props)


def UpdateBomAndRowMaterial(request, id):
    bnr = BomAndRowMaterial.objects.filter(bom=id)
    RawBomFormSet = modelformset_factory(BomAndRowMaterial, form=BomAndRowMaterialForm, extra=0)
    if request.method == "POST":
        formset = RawBomFormSet(request.POST, queryset=bnr)
        if formset.has_changed():
            if formset.is_valid():
                formset.save()
                messages.success(request, "Update Successfully.")
                return redirect('/productionplanning/update-bom/' + id)
            else:
                messages.error(request, "Update Not Successfully.")
                return redirect('/productionplanning/update-bom/' + id)
        else:
            messages.error(request, "Value Not Change.")
            return redirect('/productionplanning/update-bom/' + id)


def CopyBOM(request, id):
    copy_BOM_props['id'] = id
    bom = BOM.objects.get(id=id)
    bom_raw = BomAndRowMaterial.objects.filter(bom_id=id)
    RawBomFormSet = modelformset_factory(BomAndRowMaterial, form=BomAndRowMaterialForm2, extra=0)
    copy_BOM_props['formset'] = RawBomFormSet(queryset=bom_raw)
    copy_BOM_props["BomAndRowMaterialForm"] = BomAndRowMaterialForm3()
    mass = []
    if request.method == 'POST':
        bom_form = BOMForm2(data=request.POST, instance=bom)
        if bom_form.has_changed():
            bom_form = BOMForm2(data=request.POST)
            if bom_form.is_valid():
                bom = bom_form.save()
                for x in bom_raw:
                    dirs = {
                        'raw_material': x.raw_material,
                        'product_category': x.product_category,
                        'product_description': x.product_description,
                        'unit': x.unit,
                        'qty_required': x.qty_required,
                        'assigned_stroe': x.assigned_stroe,
                        'status': x.status,
                    }
                    form = BomAndRowMaterialForm2(data=dirs)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.bom = BOM.objects.get(id=bom.id)
                        form.save()
                        mass.append(True)
                if len(mass) == mass.count(True):
                    messages.success(request, '{} to {} Copy Successfully.'.format(id, bom.id))
                    return redirect('/productionplanning/bom/')
                else:
                    messages.error(request, 'Copy Not Successfully ')
                    return redirect('/productionplanning/bom/')
            else:
                messages.error(request, 'Copy Not Successfully ')
                return redirect('/productionplanning/bom/')
        else:
            messages.error(request, 'Value Not Change.')
            return redirect('/productionplanning/bom/')
    else:
        copy_BOM_props['bom_raw'] = bom_raw
        copy_BOM_props['forms'] = BOMForm2(instance=bom)
        if request.is_ajax():
            raw_id = request.GET.get('raw_id')
            raw = RawMaterial.objects.filter(id=raw_id).values()
            return JsonResponse({'RawMaterial': list(raw)})
        return render(request, 'PP/bom/update.html', context=copy_BOM_props)


def DeleteBOM(request, id):
    bom = BOM.objects.get(id=id)
    bom.delete()
    messages.error(request, "{} Delete Successfully.".format(id))
    return redirect('/productionplanning/bom/')
