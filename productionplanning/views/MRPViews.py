from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from ..filters.MRPFilter import MRPFilter
from ..models.BomAndRawMaterial import BomAndRowMaterial
from ..models.MRP import MRPGeneralData, MRP
from ..forms.MRPForm import MREGenetalForm, MRPForm, UpdateMRPForm
from django.contrib import messages

list_mrp_props = {
    "title": "MRP",
    "page_name": "Product",
    "subpage_name": "MRP List"
}

post_mrp_props = {
    "title": "Add MRP",
    "page_name": "Add Product",
    "subpage_name": "New MRP Add"
}

views_mrp_props = {
    "title": "View MRP",
    "page_name": "View Product",
    "subpage_name": "view MRP"
}

update_mrp_props = {
    "title": "Update MRP",
    "btn_name": "Update",
    "page_name": "Update Product",
    "subpage_name": "Update MRP"
}

copy_mrp_props = {
    "title": "Copy MRP",
    "btn_name": "Copy",
}


def ListMRP(request):
    list_mrp_props['gmrp'] = MRPGeneralData.objects.all()
    list_mrp_props['filters'] = MRPFilter()
    return render(request, 'PP/planning/mrp/list.html', context=list_mrp_props)


def FilterMRP(request):
    if request.method == 'POST':
        filter = MRPFilter(request.POST, queryset=MRPGeneralData.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'MRPGeneralData': list(filter.qs.values()),
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


def PostMRPGeneral(request):
    if request.method == "POST":
        mrp = MREGenetalForm(request.POST)
        if mrp.is_valid():
            mrp = mrp.save()
            messages.success(request, 'MRP General Created Successfully.')
            return redirect('/productionplanning/add-mrp/{}/'.format(mrp.id))
    else:
        post_mrp_props['general_data_form'] = MREGenetalForm()
        return render(request, 'PP/Planning/mrp/general_form.html', context=post_mrp_props)


def PostMRP(request, id):
    mess = []
    mrpg = MRPGeneralData.objects.get(id=id)
    bom_raw = BomAndRowMaterial.objects.filter(bom=mrpg.bom_ref_no)

    if request.method == "POST":
        raw_id = request.POST.getlist('raw_id')
        product_description = request.POST.getlist('product_description')
        unit = request.POST.getlist('unit')
        qty_required = request.POST.getlist('qty_required')
        total_reqd_qty = request.POST.getlist('total_reqd_qty')
        required_date = request.POST.getlist('required_date')
        source = request.POST.getlist('source')
        source_name = request.POST.getlist('source_name')
        action_required = request.POST.getlist('action_required')
        status = request.POST.getlist('status')
        time_to_get = request.POST.getlist('time_to_get')
        mrp_general_data = request.POST.getlist('mrp_general_data')
        for i in range(0, len(bom_raw)):
            # create a form instance and populate it with data from the request:
            form = MRPForm({'raw_id': raw_id[i], 'product_description': product_description[i],
                            'unit': unit[i], 'qty_required': qty_required[i], 'total_reqd_qty': total_reqd_qty[i],
                            'required_date': required_date[i], 'source': source[i], 'source_name': source_name[i],
                            'action_required': action_required[i], 'status': status[i], 'time_to_get': time_to_get[i],
                            'mrp_general_data': mrp_general_data[i]})
            if form.is_valid():
                mess.append(True)
                form.save()
            else:
                mess.append(False)
        if len(mess) == mess.count(True):
            messages.success(request, 'MRP Create Successfully.')
            return redirect('/productionplanning/view-mrp/{}/'.format(id))
        else:
            messages.error(request, 'MRP Not Create Successfully.')
            return redirect('/productionplanning/view-mrp/{}/'.format(id))
    else:
        post_mrp_props['bom_raw'] = bom_raw
        post_mrp_props['id'] = id
        post_mrp_props['mrpg'] = mrpg
        post_mrp_props['mrpg_id'] = mrpg.id
        return render(request, 'PP/Planning/mrp/mrp_form.html', context=post_mrp_props)


def PostMRPView(request, id):
    mrpg = MRPGeneralData.objects.get(id=id)
    mrp = MRP.objects.filter(mrp_general_data=id)
    post_mrp_props['general_data_form'] = MREGenetalForm()
    post_mrp_props['mrpg'] = mrpg
    post_mrp_props['mrpg_id'] = mrpg.id
    post_mrp_props['mrp'] = mrp
    return render(request, 'PP/Planning/mrp/mrp_form_view.html', context=post_mrp_props)


def ViewMRP(request, id):
    gmrp = MRPGeneralData.objects.get(id=id)
    mrp = MRP.objects.filter(mrp_general_data=gmrp.id)
    views_mrp_props['gmrp'] = gmrp
    views_mrp_props['mrp'] = mrp

    return render(request, 'PP/Planning/mrp/views.html', context=views_mrp_props)


def UpdateMRP(request, id):
    gmrp = MRPGeneralData.objects.get(id=id)
    gmrpForm = MREGenetalForm(instance=gmrp)
    mrp = MRP.objects.filter(mrp_general_data=id)
    MRPFOrmSet = modelformset_factory(MRP, form=UpdateMRPForm, extra=0)
    formset = MRPFOrmSet(queryset=mrp)
    update_mrp_props['id'] = id
    update_mrp_props['gmrpform'] = gmrpForm
    update_mrp_props['formset'] = formset
    if request.POST:
        gmrpForm = MREGenetalForm(request.POST, instance=gmrp)
        formset = MRPFOrmSet(request.POST, queryset=mrp)
        if gmrpForm.is_valid():
            if gmrpForm.has_changed():
                gmrpForm.save()
                messages.success(request, 'MRP General Data Update Successfully.')
                return redirect('/productionplanning/update-mrp/' + id)
            else:
                messages.error(request, "Value isn't Change.")
                return redirect('/productionplanning/update-mrp/' + id)
        if formset.is_valid():
            if formset.has_changed():
                formset.save()
                messages.success(request, 'MRP Update Successfully.')
                return redirect('/productionplanning/update-mrp/' + id)
            else:
                messages.error(request, "Value isn't Change.")
                return redirect('/productionplanning/update-mrp/' + id)
        else:
            messages.error(request, "Update isn't Successfully")
            return redirect('/productionplanning/update-mrp/' + id)
    else:
        return render(request, 'PP/Planning/mrp/update.html', context=update_mrp_props)


def CopyMRP(request, id):
    gmrp = MRPGeneralData.objects.get(id=id)
    gmrpForm = MREGenetalForm(instance=gmrp)
    mrp = MRP.objects.filter(mrp_general_data=id)
    MRPFOrmSet = modelformset_factory(MRP, form=UpdateMRPForm, extra=0)
    formset = MRPFOrmSet(queryset=mrp)
    copy_mrp_props['id'] = id
    copy_mrp_props['gmrpform'] = gmrpForm
    copy_mrp_props['formset'] = formset
    if request.POST:
        mass = []
        gmrpForm = MREGenetalForm(request.POST, instance=gmrp)
        if gmrpForm.is_valid():
            if gmrpForm.has_changed():
                gmrpForm = MREGenetalForm(request.POST)
                gmrpForm = gmrpForm.save()
                for x in mrp:
                    dirs = {
                        'mrp_general_data': MRPGeneralData.objects.get(id=gmrpForm.id),
                        'raw_id': x.raw_id,
                        'product_description': x.product_description,
                        'unit': x.unit,
                        'qty_required': x.qty_required,
                        'total_reqd_qty': x.total_reqd_qty,
                        'required_date': x.required_date,
                        'source': x.source,
                        'source_name': x.source_name,
                        'action_required': x.action_required,
                        'status': x.status,
                        'time_to_get': x.time_to_get,
                    }
                    mrp_form = MRPForm(data=dirs)
                    if mrp_form.is_valid():
                        mrp_form.save()
                        mass.append(True)
                    else:
                        mass.append(False)
                if len(mass) == mass.count(True):
                    messages.success(request, '{} to {} Copy Successfully.'.format(id, gmrpForm.id))
                    return redirect('/productionplanning/mrp/')
                else:
                    messages.error(request, 'Copy Not Successfully.')
                    return redirect('/productionplanning/mrp/')
            else:
                messages.error(request, "Value isn't Change.")
                return redirect('/productionplanning/mrp/')

    else:
        return render(request, 'PP/Planning/mrp/update.html', context=copy_mrp_props)


def DeleteMRP(request, id):
    mrp = MRPGeneralData.objects.get(pk=id)
    mrp.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/mrp/')
