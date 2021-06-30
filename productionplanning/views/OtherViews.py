from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.models.OtherProduct import Other
from productionplanning.forms.OtherForm import OtherProductForm, ViewOtherProductForm
from django.contrib import messages
from productionplanning.filters.OtherProductFilter import OtherProductFilter

list_other_props = {
    "title": "Other Product",
}

post_other_props = {
    "title": "New Other Product",
}

views_other_props = {
    "title": "View Other Product",
}

update_other_props = {
    "title": "Update Other Product",
    "btn_name": 'Update'
}

copy_other_props = {
    "title": "Copy Other Product",
    "btn_name": 'Copy'
}




def ListOther(request):
    other = Other.objects.all()
    list_other_props['other'] = other
    list_other_props['filters'] = OtherProductFilter()
    return render(request, 'PP/other/list.html', context=list_other_props)


def FilterOtherProduct(request):
    if request.method == 'POST':
        filter = OtherProductFilter(request.POST, queryset=Other.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'OtherProducts': list(filter.qs.values()),
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


def PostOther(request):
    if request.method == "POST":
        otherForms = OtherProductForm(request.POST)
        if otherForms.is_valid():
            otherForms.save()
            messages.success(request, 'Other Product Created Successfully.')
            return redirect('/productionplanning/other/')
        else:
            messages.error(request, 'Other Product Not Created Successfully.')
            return redirect('/productionplanning/other/')
    else:
        otherForms = OtherProductForm()
        post_other_props["forms"] = otherForms
        return render(request, 'PP/other/forms.html', context=post_other_props)


def ViewOther(request, id):
    instancrs = Other.objects.get(id=id)
    views_other_props['id'] = id
    views_other_props['forms'] = ViewOtherProductForm(instance=instancrs)
    return render(request, 'PP/other/views.html', context=views_other_props)


def UpdateOther(request, id):
    instancrs = Other.objects.get(id=id)
    update_other_props['id'] = id

    if request.method == "POST":
        otherForms = OtherProductForm(request.POST, instance=instancrs)
        if otherForms.has_changed():
            if otherForms.is_valid():
                otherForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/other/')
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/other/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/other/')
    else:
        update_other_props['forms'] = OtherProductForm(instance=instancrs)
        return render(request, 'PP/other/update.html', context=update_other_props)


def CopyOther(request, id):
    instancrs = Other.objects.get(id=id)
    copy_other_props['id'] = id
    if request.method == "POST":
        otherForms = OtherProductForm(request.POST, instance=instancrs)
        if otherForms.has_changed():
            otherForms = OtherProductForm(request.POST)
            if otherForms.is_valid():
                otherForms=otherForms.save()
                messages.success(request, '{} to {} Copy Successfully.'.format(id,otherForms.id ))
                return redirect('/productionplanning/other/')
            else:
                messages.error(request, '{} Copy Not Successfully.'.format(id))
                return redirect('/productionplanning/other/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/other/')
    else:
        copy_other_props['forms'] = OtherProductForm(instance=instancrs)
        return render(request, 'PP/other/update.html', context=copy_other_props)


def DeleteOther(request, id):
    other = Other.objects.get(id=id)
    other.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/other/')
