from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.models.Finished import Finished
from productionplanning.forms.FinishedForm import FinishedForm, ViewFinishedForm
from django.contrib import messages
from productionplanning.filters.FinishedFilter import FinishedFilter

list_finished_props = {
    "title": "Finished Product",
}

post_finished_props = {
    "title": "New Finished Product",
}

views_finished_props = {
    "title": "View Finished Product",
}

update_finished_props = {
    "title": "Update Finished Product",
    "btn_name": 'Update'
}

copy_finished_props = {
    "title": "Copy Finished",
    "btn_name": 'Copy'
}


def ListFinished(request):
    finished = Finished.objects.all()
    list_finished_props['finished'] = finished
    list_finished_props['filters'] = FinishedFilter()
    return render(request, 'PP/finished/list.html', context=list_finished_props)


def FilterFinished(request):
    if request.method == 'POST':
        filter = FinishedFilter(request.POST, queryset=Finished.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'Finisheds': list(filter.qs.values()),
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


def PostFinished(request):
    if request.method == "POST":
        FinishedForms = FinishedForm(request.POST)
        if FinishedForms.is_valid():
            FinishedForms.save()
            messages.success(request, 'Finished Created Successfully.')
            return redirect('/productionplanning/finished/')
        else:
            messages.error(request, 'Finished Not Created Successfully.')
            return redirect('/productionplanning/finished/')
    else:
        FinishedForms = FinishedForm()
        post_finished_props["forms"] = FinishedForms
        return render(request, 'PP/finished/forms.html', context=post_finished_props)


def ViewFinished(request, id):
    instancrs = Finished.objects.get(id=id)
    views_finished_props['id'] = id
    views_finished_props['forms'] = ViewFinishedForm(instance=instancrs)
    return render(request, 'PP/finished/views.html', context=views_finished_props)


def UpdateFinished(request, id):
    instancrs = Finished.objects.get(id=id)
    update_finished_props['id'] = id
    if request.method == "POST":
        FinishedForms = FinishedForm(request.POST, instance=instancrs)
        if FinishedForms.has_changed():
            if FinishedForms.is_valid():
                FinishedForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/finished/')
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/finished/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/finished/')
    else:
        update_finished_props['forms'] = FinishedForm(instance=instancrs)
        return render(request, 'PP/finished/update.html', context=update_finished_props)


def CopyFinished(request, id):
    instancrs = Finished.objects.get(id=id)
    copy_finished_props['id'] = id
    if request.method == "POST":
        FinishedForms = FinishedForm(request.POST, instance=instancrs)
        if FinishedForms.has_changed():
            FinishedForms = FinishedForm(request.POST)
            if FinishedForms.is_valid():
                FinishedForms = FinishedForms.save()
                messages.success(request, '{} to {} Copy Successfully.'.format(id, FinishedForms.id))
                return redirect('/productionplanning/finished/')
            else:
                messages.error(request, '{} Copy Not Successfully.'.format(id))
                return redirect('/productionplanning/finished/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/finished/')
    else:
        copy_finished_props['forms'] = FinishedForm(instance=instancrs)
        return render(request, 'PP/finished/update.html', context=copy_finished_props)


def DeleteFinished(request, id):
    finished = Finished.objects.get(id=id)
    finished.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/finished/')
