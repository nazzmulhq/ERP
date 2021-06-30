from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.models.SemiFinished import SemiFinished
from productionplanning.forms.SemiFinishedForm import SemiFinishedForm, ViewSemiFinishedForm
from django.contrib import messages
from productionplanning.filters.SemiFinishedFilter import SemiFinishedFilter

list_semi_finished_props = {
    "title": "Semi Finished Product",
}

post_semi_finished_props = {
    "title": "New Semi Finished Product",
}

views_semi_finished_props = {
    "title": "View Semi Finished Product",
}

update_semi_finished_props = {
    "title": "Update Semi Finished Product",
    "btn_name": 'Update'
}


copy_semi_finished_props = {
    "title": "Copy Semi Finished",
    "btn_name": 'Copy'
}

def ListSemiFinished(request):
    allSemiFinished = SemiFinished.objects.all()
    list_semi_finished_props['products'] = allSemiFinished

    list_semi_finished_props['filters'] = SemiFinishedFilter()
    return render(request, 'PP/semifinished/list.html', context=list_semi_finished_props)


def FilterSemiFinished(request):
    if request.method == 'POST':
        filter = SemiFinishedFilter(request.POST, queryset=SemiFinished.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'SemiFinisheds': list(filter.qs.values()),
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


def PostSemiFinished(request):
    if request.method == "POST":
        SemiFinishedForms = SemiFinishedForm(request.POST)
        if SemiFinishedForms.is_valid():
            SemiFinishedForms.save()
            messages.success(request, 'Semi Finished Created Successfully.')
            return redirect('/productionplanning/semi-finished/')
        else:
            messages.error(request, 'Semi Finished Not Created Successfully.')
            return redirect('/productionplanning/semi-finished/')
    else:
        SemiFinishedForms = SemiFinishedForm()
        post_semi_finished_props["forms"] = SemiFinishedForms
        return render(request, 'PP/semifinished/forms.html', context=post_semi_finished_props)


def ViewSemiFinished(request, id):
    instancrs = SemiFinished.objects.get(id=id)
    views_semi_finished_props['id'] = id
    views_semi_finished_props['forms'] = ViewSemiFinishedForm(instance=instancrs)
    return render(request, 'PP/semifinished/views.html', context=views_semi_finished_props)


def UpdateSemiFinished(request, id):
    instancrs = SemiFinished.objects.get(id=id)
    update_semi_finished_props['id'] = id

    if request.method == "POST":
        SemiFinishedForms = SemiFinishedForm(request.POST, instance=instancrs)
        if SemiFinishedForms.has_changed():
            if SemiFinishedForms.is_valid():
                SemiFinishedForms.save()
                messages.success(request, "{} Update Successfully.".format(id))
                return redirect('/productionplanning/semi-finished/')
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/semi-finished/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/semi-finished/')
    else:
        update_semi_finished_props['forms'] = SemiFinishedForm(instance=instancrs)
        return render(request, 'PP/semifinished/update.html', context=update_semi_finished_props)


def CopySemiFinished(request, id):
    instancrs = SemiFinished.objects.get(id=id)
    copy_semi_finished_props['id'] = id
    if request.method == "POST":
        SemiFinishedForms = SemiFinishedForm(request.POST, instance=instancrs)
        if SemiFinishedForms.has_changed():
            SemiFinishedForms = SemiFinishedForm(data=request.POST)
            if SemiFinishedForms.is_valid():
                SemiFinishedForms=SemiFinishedForms.save()
                messages.success(request, "{} to {} Copy Successfully.".format(id, SemiFinishedForms.id))
                return redirect('/productionplanning/semi-finished/')
            else:
                messages.error(request, '{} Copy Not Successfully.'.format(id))
                return redirect('/productionplanning/semi-finished/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/semi-finished/')
    else:
        copy_semi_finished_props['forms'] = SemiFinishedForm(instance=instancrs)
        return render(request, 'PP/semifinished/update.html', context=copy_semi_finished_props)


def DeleteSemiFinished(request, id):
    semi_finished = SemiFinished.objects.get(id=id)
    semi_finished.delete()
    messages.error(request, "{} Delete Successfully".format(id))
    return redirect('/productionplanning/semi-finished/')
