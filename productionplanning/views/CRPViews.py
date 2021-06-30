from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from ..filters.CRPFilter import CRPFilter
from ..forms.CRPForm import UpdateCRPForm, CRPTrackForm, AddCRPForm
from django.forms import modelformset_factory
from datetime import datetime, timedelta
from ..forms.ProductCenterForm import CapacitySchedulingFormCRP
from ..models.CRP import CRPTrack, CRP
from ..models.Finished import Finished
from ..models.OperationList import OperationList
from ..models.ProductCenter import ProductCenter, CapacityScheduling
from ..models.OperationSequence import OperationSequence
from django.contrib import messages

list_crp_props = {
    "title": "CRP",

}

post_crp_props = {
    "title": "Add CRP",

}

views_crp_props = {
    "title": "View CRP",

}

update_crp_props = {
    "title": "Update CRP",
    'btn_name': 'Update'
}

copy_crp_props = {
    "title": "Copy CRP",
    'btn_name': 'Copy'

}


def ListCRP(request):
    if request.method == "GET":
        crp_track = CRPTrack.objects.all()
        list_crp_props['crp_track'] = crp_track
        list_crp_props['filters'] = CRPFilter()
        return render(request, 'PP/planning/crp/list.html', context=list_crp_props)


def FilterCRP(request):
    if request.method == 'POST':
        filter = CRPFilter(request.POST, queryset=CRPTrack.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'CRPTrack': list(filter.qs.values()),
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


def PostCRP(request):
    if request.method == "POST":
        finish = request.POST.get('finished_no')
        order_ref = request.POST.get('order_ref')
        order_qty = request.POST.get('order_qty')

        if request.is_ajax():
            finish = Finished.objects.get(id=finish)
            opl = OperationList.objects.filter(id=finish.operations_list.id).values()
            opsec = OperationSequence.objects.filter(operation_list=finish.operations_list).values()
            crp = []
            for ops in opsec:
                pc = ProductCenter.objects.get(id=ops['production_center_id'])
                cs = CapacityScheduling.objects.filter(ProductCenterId=ops['production_center_id']).last()
                crp.append({
                    'operationSequence': ops['operationSequence'],
                    'productioncneter': pc.product_center_name,
                    'AvalStartDate': cs.Date,
                    'reqdcapunit': ops['reqdcapunit'],
                    'ReqdMcHrByUnit': ops['totaltime'],
                    'AvalStartTime': cs.EndTime,
                    'AvalMcHrOrDay': cs.BalMcOrHour,
                    'NoOfMCByResAval': int(pc.NoOfMByC) - int(cs.NoOfMCAlloctd),
                    'AvalCAPByDay': cs.BalanceCap,
                })

            crp_track_form = CRPTrackForm({'finished': finish,
                                           'operationlist': finish.operations_list.id,
                                           'product_description': finish.product_description,
                                           'order_ref': order_ref,
                                           'order_qty': order_qty
                                           })

            if crp_track_form.is_valid():
                crp_track_form = crp_track_form.save()
                return JsonResponse({
                    'mass': "success",
                    'operation_scheduling': list(opsec),
                    'crps': crp,
                    'CRPTrack': list(CRPTrack.objects.filter(id=crp_track_form.id).values())
                }, status=200)

        operationSequence = request.POST.getlist('operationSequence')
        productioncneter = request.POST.getlist('productioncneter')
        AvalStartDate = request.POST.getlist('AvalStartDate')
        StartDate = request.POST.getlist('StartDate')
        NoOfMCByResAval = request.POST.getlist('NoOfMCByResAval')
        AvalCAPByDay = request.POST.getlist('AvalCAPByDay')
        reqdcapunit = request.POST.getlist('reqdcapunit')
        ReqdCAPByDay = request.POST.getlist('ReqdCAPByDay')
        AvalMcHrOrDay = request.POST.getlist('AvalMcHrOrDay')
        ReqdMcHrByUnit = request.POST.getlist('ReqdMcHrByUnit')
        ReqdMcHour = request.POST.getlist('ReqdMcHour')
        AvalStartTime = request.POST.getlist('AvalStartTime')
        StartTime = request.POST.getlist('StartTime')
        EndTime = request.POST.getlist('EndTime')
        EndDate = request.POST.getlist('EndDate')
        NoOfMcByRes = request.POST.getlist('NoOfMcByRes')
        mc_id_no = request.POST.getlist('mc_id_no')
        crp_track = request.POST.getlist('crp_track')
        mass = False
        if len(operationSequence) != 0:
            for x in range(0, len(operationSequence)):
                crp = AddCRPForm({
                    'crp_track': CRPTrack.objects.get(id=crp_track[x]),
                    'operationSequence': operationSequence[x],
                    "productioncneter": productioncneter[x],
                    "reqdcapunit": reqdcapunit[x],
                    "ReqdMcHrByUnit": ReqdMcHrByUnit[x],
                    "AvalStartDate": AvalStartDate[x],
                    'AvalStartTime': AvalStartTime[x],
                    "NoOfMCByResAval": NoOfMCByResAval[x],
                    "AvalCAPByDay": AvalCAPByDay[x],
                    'AvalMcHrOrDay': AvalMcHrOrDay[x],
                    'StartDate': StartDate[x],
                    'ReqdCAPByDay': ReqdCAPByDay[x],
                    'ReqdMcHour': ReqdMcHour[x],
                    'StartTime': StartTime[x],
                    'EndTime': EndTime[x],
                    'EndDate': EndDate[x],
                    'NoOfMcByRes': NoOfMcByRes[x],
                    'mc_id_no': mc_id_no[x]
                })

                if crp.is_valid():
                    crp = crp.save()
                    crp_tracks = CRPTrack.objects.get(id=crp.crp_track)

                    BalanceCap = int(crp.AvalCAPByDay) - int(crp.ReqdCAPByDay)

                    cs = CapacitySchedulingFormCRP({
                        'ProductCenterId': ProductCenter.objects.get(product_center_name=crp.productioncneter),
                        'Date': crp.AvalStartDate,
                        'AvalCapOrDay': crp.AvalCAPByDay,
                        'CapALlloctdTo': crp_tracks.finished.id,
                        'AlloctdCap': crp.ReqdCAPByDay,
                        'BalanceCap': BalanceCap,
                        'AvalMcOrResHour': crp.AvalMcHrOrDay,
                        'ReqdMcOrResHour': crp.ReqdMcHour,
                        'BalMcOrHour': str(float(crp.AvalMcHrOrDay) - float(crp.ReqdMcHour)),
                        'StartTime': crp.StartTime,
                        'EndTime': crp.EndTime,
                        'NoOfMCAlloctd': crp.NoOfMcByRes,

                    })
                    if cs.is_valid():
                        cs.save()
                    if BalanceCap == 0:
                        AvalStartDates = datetime.strptime(str(crp.AvalStartDate), '%Y-%m-%d')
                        AvalStartDates = AvalStartDates + timedelta(days=1)
                        pc = ProductCenter.objects.get(product_center_name=crp.productioncneter)
                        csl = CapacityScheduling.objects.filter(ProductCenterId=pc.id).first()
                        cs = CapacitySchedulingFormCRP({
                            'ProductCenterId': ProductCenter.objects.get(product_center_name=crp.productioncneter),
                            'Date': AvalStartDates,
                            'AvalCapOrDay': csl.AvalCapOrDay,
                            'CapALlloctdTo': csl.CapALlloctdTo,
                            'AlloctdCap': csl.AlloctdCap,
                            'BalanceCap': csl.BalanceCap,
                            'AvalMcOrResHour': csl.AvalMcOrResHour,
                            'ReqdMcOrResHour': csl.ReqdMcOrResHour,
                            'BalMcOrHour': csl.BalMcOrHour,
                            'StartTime': csl.StartTime,
                            'EndTime': csl.EndTime,
                            'NoOfMCAlloctd': csl.NoOfMCAlloctd,
                        })
                        if cs.is_valid():
                            cs.save()
                    mass = True
                else:
                    mass = False
            if mass:
                messages.success(request, 'CRP Created Successfully.')
            return HttpResponseRedirect(reverse('productionplanning:CRP', args={crp_track[0]}))
        else:
            messages.error(request, 'CRP Not Created Successfully.')

        return render(request, 'PP/Planning/crp/general_data_form.html', context=post_crp_props)
    else:
        return render(request, 'PP/Planning/crp/general_data_form.html', context=post_crp_props)


def AddCRP(request, id):
    crp_track = CRPTrack.objects.get(id=id)
    crp = CRP.objects.filter(crp_track=crp_track.id)
    post_crp_props['crp_track'] = crp_track
    post_crp_props['crp'] = crp
    return render(request, 'PP/Planning/crp/add_crp.html', context=post_crp_props)


def ViewCRP(request, id):
    crp_track = CRPTrack.objects.get(id=id)
    crp = CRP.objects.filter(crp_track=crp_track.id)
    views_crp_props['crp_track'] = crp_track
    views_crp_props['crp'] = crp
    return render(request, 'PP/Planning/crp/views.html', context=views_crp_props)


def UpdateCRP(request, id):
    crp_track = CRPTrack.objects.get(id=id)
    crp = CRP.objects.filter(crp_track=crp_track.id)
    update_crp_props['crp_track'] = crp_track
    update_crp_props['crp'] = crp
    CRPFoemSet = modelformset_factory(CRP, form=UpdateCRPForm, extra=0)
    formset = CRPFoemSet(queryset=crp)
    update_crp_props['formset'] = formset
    if request.POST:
        formset = CRPFoemSet(request.POST, queryset=crp)
        if formset.has_changed():
            if formset.is_valid():
                formset.save()
                messages.success(request, 'CRP Update Successfully.')
                return HttpResponseRedirect(reverse('productionplanning:UpdateCRP', args={crp_track.id}))
            else:
                messages.error(request, 'CRP Form is not valid.')
                return HttpResponseRedirect(reverse('productionplanning:UpdateCRP', args={crp_track.id}))
        else:
            messages.error(request, 'Value is not Change.')
            return HttpResponseRedirect(reverse('productionplanning:UpdateCRP', args={crp_track.id}))
    else:
        return render(request, 'PP/Planning/crp/update_crp.html', context=update_crp_props)


def CopyCRP(request, id):
    crp_track = CRPTrack.objects.get(id=id)
    crp = CRP.objects.filter(crp_track=crp_track.id)
    copy_crp_props['crp_track'] = crp_track
    copy_crp_props['crp'] = crp
    CRPFoemSet = modelformset_factory(CRP, form=UpdateCRPForm, extra=0)
    formset = CRPFoemSet(queryset=crp)
    copy_crp_props['formset'] = formset
    if request.POST:
        mass = []
        crp_trackForm = CRPTrackForm(data={
            'finished': crp_track.finished,
            'operationlist': crp_track.operationlist,
            'product_description': crp_track.product_description,
            'order_ref': crp_track.order_ref,
            'order_qty': crp_track.order_qty,
        })
        if crp_trackForm.is_valid():
            crp_trackForm = crp_trackForm.save()
            for x in crp:
                dirs = {
                    'crp_track': CRPTrack.objects.get(id=crp_trackForm.id),
                    'operationSequence': x.operationSequence,
                    'productioncneter': x.productioncneter,
                    'AvalStartDate': x.AvalStartDate,
                    'StartDate': x.StartDate,
                    'reqdcapunit': x.reqdcapunit,
                    'ReqdMcHrByUnit': x.ReqdMcHrByUnit,
                    'AvalStartTime': x.AvalStartTime,
                    'AvalMcHrOrDay': x.AvalMcHrOrDay,
                    'NoOfMCByResAval': x.NoOfMCByResAval,
                    'AvalCAPByDay': x.AvalCAPByDay,
                    'ReqdCAPByDay': x.ReqdCAPByDay,
                    'ReqdMcHour': x.ReqdMcHour,
                    'StartTime': x.StartTime,
                    'EndTime': x.EndTime,
                    'EndDate': x.EndDate,
                    'NoOfMcByRes': x.NoOfMcByRes,
                    'mc_id_no': x.mc_id_no,
                }
                crp_form = UpdateCRPForm(data=dirs)
                print(2,crp_form.is_valid())
                if crp_form.is_valid():
                    crp_form = crp_form.save(commit=False)
                    crp_form.crp_track = CRPTrack.objects.get(id=crp_trackForm.id)
                    crp_form.save()
                    mass.append(True)
                else:
                    mass.append(False)
            if len(mass) == mass.count(True):
                messages.success(request, '{} to {} Copy Successfully.'.format(id, crp_trackForm.id))
                return redirect('/productionplanning/crp/')
            else:
                messages.error(request, 'Copy Not Successfully.')
                return redirect('/productionplanning/crp/')
        else:
            messages.error(request, "CRP Form isn't Valid.")
            return redirect('/productionplanning/crp/')

    else:
        return render(request, 'PP/Planning/crp/update_crp.html', context=copy_crp_props)


def DeleteCRP(request, id):
    crp = CRPTrack.objects.get(id=id)
    crp.delete()
    messages.error(request, '{} Delete Successfully.'.format(id))
    return redirect('/productionplanning/crp/')
