from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import JsonResponse
from productionplanning.models.OperationList import OperationList
from productionplanning.models.OperationSequence import OperationSequence
from productionplanning.forms.OperationListForm import OperationListForm
from productionplanning.forms.OperationListForm import OperationSequenceForm
from django.forms import modelformset_factory
from django.contrib import messages
from productionplanning.filters.OperationListFilter import OperationListFilter

list_operation_list_props = {
    "title": "Operation List",
}

post_operation_list_props = {
    "title": "New Operation List",
}

views_operation_list_props = {
    "title": "View Operation List",
}

update_operation_list_props = {
    "title": "Update Operation List",
    "btn_name": "Update",
}

copy_operation_list_props = {
    "title": "Copy Operation List",
    "btn_name": "Copy",
}


def ListOperationList(request):
    OperationLists = OperationList.objects.all()
    list_operation_list_props['products'] = OperationLists
    list_operation_list_props['filters'] = OperationListFilter()
    return render(request, 'PP/operationlist/list.html', context=list_operation_list_props)


def FilterOperationList(request):
    if request.method == 'POST':
        filter = OperationListFilter(request.POST, queryset=OperationList.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'OperationLists': list(filter.qs.values()),
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


def PostOperationList(request):
    if request.method == 'POST':
        OperationListForms = OperationListForm(request.POST)
        if OperationListForms.is_valid():
            opl = OperationListForms.save()
            messages.success(request, 'Created Successfully.'.format(id))
            return HttpResponseRedirect(reverse('productionplanning:PostOperationSequence', args=(opl.id,)))
        else:
            messages.error(request, 'Created Not Successfully.'.format(id))
        return redirect('/productionplanning/add-operation-list/')
    else:
        OperationListForms = OperationListForm()
        OperationSequenceForms = OperationSequenceForm()
        post_operation_list_props["OperationListForms"] = OperationListForms
        post_operation_list_props["OperationSequenceForms"] = OperationSequenceForms
        return render(request, 'PP/operationlist/operationlist.html', context=post_operation_list_props)


def PostOperationSequence(request, id):
    ol = OperationList.objects.get(id=id)
    os = OperationSequence.objects.filter(operation_list_id=id)
    if request.method == 'POST':
        OperationSequenceForms = OperationSequenceForm(request.POST)
        if OperationSequenceForms.is_valid():
            operation_sequence = OperationSequenceForms.save(commit=False)
            operation_sequence.operation_list = ol
            operation_sequence.save()
            messages.success(request, '{} Created Successfully.'.format(id))
            return redirect('/productionplanning/add-operation-sequence/{}/'.format(id))
        else:
            messages.error(request, 'Created Not Successfully.'.format(id))
        return redirect('/productionplanning/add-operation-list/')
    else:
        OperationListForms = OperationListForm(instance=ol)
        OperationSequenceForms = OperationSequenceForm()
        post_operation_list_props["OperationList"] = ol
        post_operation_list_props["id"] = ol.id
        post_operation_list_props["OperationSequence"] = os
        post_operation_list_props["OperationListForms"] = OperationListForms
        post_operation_list_props["OperationSequenceForms"] = OperationSequenceForms
        return render(request, 'PP/operationlist/operation_sequence.html', context=post_operation_list_props)


def PostFinishOperationSequence(request, id):
    ol = OperationList.objects.get(id=id)
    if request.method == 'POST':
        OperationSequenceForms = OperationSequenceForm(request.POST)
        if OperationSequenceForms.is_valid():
            operation_sequence = OperationSequenceForms.save(commit=False)
            operation_sequence.operation_list = ol
            operation_sequence.save()
            messages.success(request, 'Created Successfully.')
            return redirect('/productionplanning/operation-list/')
        else:
            messages.error(request, 'Not Created Successfully.')
            return redirect('/productionplanning/operation-list/')


def ViewOperationList(request, id):
    opl = OperationList.objects.get(id=id)
    ops = OperationSequence.objects.filter(operation_list=opl.id)
    views_operation_list_props['id'] = id
    views_operation_list_props['opl'] = opl
    views_operation_list_props['OperationSequence'] = ops
    return render(request, 'PP/operationlist/views.html', context=views_operation_list_props)


def UpdateOperationList(request, id):
    opl = OperationList.objects.get(id=id)
    ops = OperationSequence.objects.filter(operation_list=opl.id)
    update_operation_list_props['id'] = id
    OperationSequenceFormSet = modelformset_factory(OperationSequence, form=OperationSequenceForm, extra=0)
    formset = OperationSequenceFormSet(queryset=ops)
    if request.method == "POST":
        olf = OperationSequenceForm(request.POST)
        OperationListForms = OperationListForm(request.POST, instance=opl)
        OperationSequenceFormSet = modelformset_factory(OperationSequence, form=OperationSequenceForm, extra=0)
        formset = OperationSequenceFormSet(request.POST, queryset=ops)

        if olf.is_valid():
            olf = olf.save(commit=False)
            olf.operation_list = opl
            messages.success(request, 'Operation Sequence Created Successfully.')
            olf.save()
            return redirect('/productionplanning/update-operation-list/' + id)
        if OperationListForms.is_valid():
            if OperationListForms.has_changed():
                OperationListForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/update-operation-list/' + id)
            else:
                messages.error(request, '{} Value Not Change.'.format(id))
                return redirect('/productionplanning/update-operation-list/' + id)
        if formset.is_valid():
            if formset.has_changed():
                formset.save()
                messages.success(request, 'Update Successfully.')
                return redirect('/productionplanning/update-operation-list/' + id)
            else:
                messages.error(request, '{} Value Not Change.'.format(id))
                return redirect('/productionplanning/update-operation-list/' + id)
        return redirect('/productionplanning/operation-list/')
    else:
        update_operation_list_props['formset'] = formset
        update_operation_list_props['OperationListForm'] = OperationListForm(instance=opl)
        update_operation_list_props['OperationSequenceForms'] = OperationSequenceForm()
        return render(request, 'PP/operationlist/update.html', context=update_operation_list_props)


def UpdateOperationSequence(request, id):
    if request.method == "POST":
        ops = OperationSequence.objects.get(pk=id)
        OperationSequenceForms = OperationSequenceForm(request.POST, instance=ops)
        if OperationSequenceForms.has_changed():
            if OperationSequenceForms.is_valid():
                OperationSequenceForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/update-operation-list/' + ops.operation_list_id)
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/update-operation-list/' + ops.operation_list_id)
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/update-operation-list/' + ops.operation_list_id)


def CopyOperationList(request, id):
    opl = OperationList.objects.get(id=id)
    ops = OperationSequence.objects.filter(operation_list=opl.id)
    copy_operation_list_props['id'] = id
    OperationSequenceFormSet = modelformset_factory(OperationSequence, form=OperationSequenceForm, extra=0)
    formset = OperationSequenceFormSet(queryset=ops)
    mass = []
    if request.method == "POST":
        olf = OperationSequenceForm(request.POST)
        OperationListForms = OperationListForm(request.POST, instance=opl)
        if olf.is_valid():
            olf = olf.save(commit=False)
            olf.operation_list = opl
            messages.success(request, 'Operation Sequence Created Successfully.')
            olf.save()
            return redirect('/productionplanning/copy-operation-list/' + id)
        if OperationListForms.is_valid():
            if OperationListForms.has_changed() and OperationListForm(request.POST).is_valid():
                OperationListForms = OperationListForm(request.POST)
                OperationListForms = OperationListForms.save()
                for x in ops:
                    dirs = {
                        'operationSequence': x.operationSequence,
                        'baseunit': x.baseunit,
                        'reqdcapunit': x.reqdcapunit,
                        'standardtime': x.standardtime,
                        'allowancetime': x.allowancetime,
                        'totaltime': x.totaltime,
                        'componentsuses': x.componentsuses,
                        'toolsrequired': x.toolsrequired,
                        'inspectioncenter': x.inspectioncenter,
                        'exceptionmsg': x.exceptionmsg
                    }
                    forms = OperationSequenceForm(data=dirs)
                    if forms.is_valid():
                        forms = forms.save(commit=False)
                        forms.operation_list = OperationList.objects.get(id=OperationListForms.id)
                        forms.production_center = x.production_center
                        forms.save()
                        mass.append(True)
                    else:
                        mass.append(False)
                if len(mass) == mass.count(True):
                    messages.success(request, '{} to {} Copy Successfully.'.format(id, OperationListForms.id))
                    return redirect('/productionplanning/operation-list/')
                else:
                    messages.error(request, '{} Not Copy Successfully.'.format(id))
                    return redirect('/productionplanning/operation-list/')
            else:
                messages.error(request, '{} Value Not Change.'.format(id))
                return redirect('/productionplanning/operation-list/')

        return redirect('/productionplanning/operation-list/')
    else:
        copy_operation_list_props['formset'] = formset
        copy_operation_list_props['OperationListForm'] = OperationListForm(instance=opl)
        copy_operation_list_props['OperationSequenceForms'] = OperationSequenceForm()
        return render(request, 'PP/operationlist/update.html', context=copy_operation_list_props)


def DeleteOperationList(request, id):
    opl = OperationList.objects.get(id=id)
    opl.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/operation-list/')
