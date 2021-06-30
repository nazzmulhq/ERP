from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.filters.SubmissionAndApprovalFilter import SubmissionAndApprovalFilter
from productionplanning.models.SubmissionAndApproval import SubmissionAndApproval
from productionplanning.forms.SubmissionAndApprovalForm import SubmissionAndApprovalForm
from django.contrib import messages

list_submission_and_approval_props = {
    "title": "Submission & Approval",
}

post_submission_and_approval_props = {
    "title": "New Submission & Approval",
}

views_submission_and_approval_props = {
    "title": "View Submission & Approval",
}

update_submission_and_approval_props = {
    "title": "Update Submission & Approval",
    "btn_name": 'Update'
}

copy_submission_and_approval_props = {
    "title": "Copy Submission & Approval",
    "btn_name": 'Copy'
}


def ListSubmissionAndApproval(request):
    list_submission_and_approval_props.update({"lengths": len(SubmissionAndApproval.objects.all())})
    allSubmissionAndApproval = SubmissionAndApproval.objects.all()
    filter = SubmissionAndApprovalFilter()
    list_submission_and_approval_props['SubmissionAndApprovals'] = allSubmissionAndApproval
    list_submission_and_approval_props['filters'] = filter

    return render(request, 'PP/submissionandapproval/list.html', context=list_submission_and_approval_props)


def FilterSubmissionAndApproval(request):
    if request.method == 'POST':
        filter = SubmissionAndApprovalFilter(request.POST, queryset=SubmissionAndApproval.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'SubmissionAndApprovals': list(filter.qs.values()),
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


def PostSubmissionAndApproval(request):
    if request.method == "POST":
        SubmissionAndApprovalForms = SubmissionAndApprovalForm(request.POST)
        if SubmissionAndApprovalForms.is_valid():
            SubmissionAndApprovalForms.save()
            messages.success(request, 'Submission & Approval Created Successfully.')
            return redirect('/productionplanning/submission-and-approval/')
        else:
            messages.error(request, 'Submission & Approval Not Created Successfully.')
            return redirect('/productionplanning/submission-and-approval/')
    else:
        post_submission_and_approval_props['forms'] = SubmissionAndApprovalForm()
        return render(request, 'PP/submissionandapproval/forms.html', context=post_submission_and_approval_props)


def ViewSubmissionAndApproval(request, id):
    instancrs = SubmissionAndApproval.objects.get(id=id)
    views_submission_and_approval_props['id'] = id
    views_submission_and_approval_props['forms'] = SubmissionAndApprovalForm(instance=instancrs)
    return render(request, 'PP/submissionandapproval/views.html', context=views_submission_and_approval_props)


def UpdateSubmissionAndApproval(request, id):
    instancrs = SubmissionAndApproval.objects.get(id=id)
    update_submission_and_approval_props['id'] = id
    if request.method == "POST":
        SubmissionAndApprovalForms = SubmissionAndApprovalForm(request.POST, instance=instancrs)
        if SubmissionAndApprovalForms.has_changed():
            if SubmissionAndApprovalForms.is_valid():
                SubmissionAndApprovalForms.save()
                messages.success(request, '{} Update Successfully.'.format(id))
                return redirect('/productionplanning/submission-and-approval/')
            else:
                messages.error(request, '{} Update Not Successfully.'.format(id))
                return redirect('/productionplanning/submission-and-approval/')
        else:
            messages.error(request, '{} Value Not Change.'.format(id))
            return redirect('/productionplanning/submission-and-approval/')
    else:
        update_submission_and_approval_props['forms'] = SubmissionAndApprovalForm(instance=instancrs)
        return render(request, 'PP/submissionandapproval/update.html', context=update_submission_and_approval_props)


def CopySubmissionAndApproval(request, id):
    instancrs = SubmissionAndApproval.objects.get(id=id)
    if request.method == "POST":
        SubmissionAndApprovalForms = SubmissionAndApprovalForm(request.POST, instance=instancrs)
        if SubmissionAndApprovalForms.has_changed():
            SubmissionAndApprovalForms = SubmissionAndApprovalForm(data=request.POST)
            if SubmissionAndApprovalForms.is_valid():
                forms = SubmissionAndApprovalForms.save()
                messages.success(request, '{} to {} Copy Successfully.'.format(id, forms.id))
                return redirect('/productionplanning/submission-and-approval/')
            else:
                messages.error(request, '{} Copy Is Not Successful.'.format(id))
                return redirect('/productionplanning/submission-and-approval/')
        else:
            messages.error(request, '{} Value Is Not Change.'.format(id))
            return redirect('/productionplanning/submission-and-approval/')
    else:
        copy_submission_and_approval_props['id'] = id
        copy_submission_and_approval_props['forms'] = SubmissionAndApprovalForm(instance=instancrs)
        return render(request, 'PP/submissionandapproval/update.html', context=copy_submission_and_approval_props)


def DeleteSubmissionAndApproval(request, id):
    submission_and_approval = SubmissionAndApproval.objects.get(id=id)
    submission_and_approval.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/submission-and-approval/')
