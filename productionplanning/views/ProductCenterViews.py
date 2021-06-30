from django.http import JsonResponse
from django.shortcuts import render, redirect
from productionplanning.models.ProductCenter import ProductCenter, CapacityScheduling
from productionplanning.forms.ProductCenterForm import ProductCenterForm, ViewProductCenterForm, CapacitySchedulingForm, \
    ViewCapacitySchedulingForm
from django.forms import modelformset_factory
from django.contrib import messages
from productionplanning.filters.ProductCenterFilter import ProductCenterFilter

list_product_center_props = {
    "title": "Production Center",
}

post_product_center_props = {
    "title": "New Production Center",
    "alert": False
}

views_product_center_props = {
    "title": "View Production Center",
}

update_product_center_props = {
    "title": "Update Production Center",
    "SchedulingForms": dict(),
    "btn_name": 'Update'
}

copy_product_center_props = {
    "title": "Copy Production Center",
    "btn_name": 'Copy'
}


def ListProductCenter(request):
    list_product_center_props['products'] = ProductCenter.objects.all()
    list_product_center_props['filters'] = ProductCenterFilter()
    return render(request, 'PP/productcenter/list.html', context=list_product_center_props)


def FilterProductCenter(request):
    if request.method == 'POST':
        filter = ProductCenterFilter(request.POST, queryset=ProductCenter.objects.all())
        if filter.is_valid():
            if len(filter.qs.values()) != 0:
                return JsonResponse({
                    'ProductCenters': list(filter.qs.values()),
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


def PostProductCenter(request):
    if request.method == "POST":
        ProductCenterForms = ProductCenterForm(request.POST)
        CapacitySchedulingForms = CapacitySchedulingForm(request.POST)
        if ProductCenterForms.is_valid() and CapacitySchedulingForms.is_valid():
            ProductCenterForms = ProductCenterForms.save()
            CapacitySchedulingForms = CapacitySchedulingForms.save(commit=False)
            CapacitySchedulingForms.ProductCenterId_id = ProductCenterForms.id
            CapacitySchedulingForms.save()
            messages.success(request, "Product Center & Capacity Scheduling Created Successfully.")
            return redirect('/productionplanning/product-center/')
        else:
            messages.error(request, "Product Center & Capacity Scheduling Is Not Created Successfully.")
            return redirect('/productionplanning/product-center/')
    else:
        post_product_center_props["ProductCenterForm"] = ProductCenterForm()
        post_product_center_props["CapacitySchedulingForm"] = CapacitySchedulingForm()
        return render(request, 'PP/productcenter/forms.html', context=post_product_center_props)


def ViewProductCenter(request, id):
    views_product_center_props['id'] = id
    views_product_center_props['ProductCenter'] = ProductCenter.objects.get(id=id)
    views_product_center_props['capacity_scheduling'] = CapacityScheduling.objects.filter(ProductCenterId=id)
    return render(request, 'PP/productcenter/views.html', context=views_product_center_props)


def UpdateProductCenter(request, id):
    ProductCenterInstancrs = ProductCenter.objects.get(id=id)
    CapacitySchedulingInstancrs = CapacityScheduling.objects.filter(ProductCenterId=id)
    CapacitySchedulingFormSet = modelformset_factory(CapacityScheduling, form=CapacitySchedulingForm, extra=0)
    formset = CapacitySchedulingFormSet(queryset=CapacitySchedulingInstancrs)
    update_product_center_props['id'] = id

    if request.method == "POST":
        CapacitySchedulingForms = CapacitySchedulingForm(request.POST)
        ProductCenterForms = ProductCenterForm(request.POST, instance=ProductCenterInstancrs)
        if ProductCenterForms.has_changed():
            if ProductCenterForms.is_valid():
                ProductCenterForms.save()
                messages.success(request, "{} Update Successfully".format(id))
                return redirect('/productionplanning/update-product-center/' + id)
        else:
            messages.error(request, "{} Value Not Change".format(id))
            return redirect('/productionplanning/update-product-center/' + id)
        if CapacitySchedulingForms.is_valid():
            CapacitySchedulingForms = CapacitySchedulingForms.save(commit=False)
            CapacitySchedulingForms.ProductCenterId_id = id
            CapacitySchedulingForms.save()
            messages.success(request, "Capacity Scheduling Create Successfully")
            return redirect('/productionplanning/update-product-center/' + id)
        else:
            messages.error(request, "Capacity Scheduling Not Create Successfully")
            return redirect('/productionplanning/update-product-center/' + id)
    else:
        update_product_center_props['formset'] = formset
        update_product_center_props['ProductCenter'] = ProductCenterForm(instance=ProductCenterInstancrs)
        update_product_center_props["CapacitySchedulingForm"] = CapacitySchedulingForm()
        return render(request, 'PP/productcenter/update.html', context=update_product_center_props)


def UpdateCapacityScheduling(request, id):
    if request.method == "POST":
        cs = CapacityScheduling.objects.filter(ProductCenterId=id)
        CapacitySchedulingFormSet = modelformset_factory(CapacityScheduling, form=CapacitySchedulingForm, extra=0)

        formset = CapacitySchedulingFormSet(request.POST, queryset=cs)
        if formset.has_changed():
            if formset.is_valid():
                formset.save()
                messages.success(request, "Update Successfully")
                return redirect('/productionplanning/update-product-center/' + id)
            else:
                messages.error(request, "Update Not Successfully")
                return redirect('/productionplanning/update-product-center/' + id)
        else:
            messages.error(request, "Value Not Change")
            return redirect('/productionplanning/update-product-center/' + id)


def CopyProductCenter(request, id):
    ProductCenterInstancrs = ProductCenter.objects.get(id=id)
    CapacitySchedulingInstancrs = CapacityScheduling.objects.filter(ProductCenterId=id)
    CapacitySchedulingFormSet = modelformset_factory(CapacityScheduling, form=CapacitySchedulingForm, extra=0)
    formset = CapacitySchedulingFormSet(queryset=CapacitySchedulingInstancrs)
    copy_product_center_props['id'] = id
    mass = []
    if request.method == "POST":
        CapacitySchedulingForms = CapacitySchedulingForm(request.POST)
        ProductCenterForms = ProductCenterForm(request.POST, instance=ProductCenterInstancrs)
        if ProductCenterForms.has_changed():
            if CapacitySchedulingForms.is_valid():
                CapacitySchedulingForms = CapacitySchedulingForms.save(commit=False)
                CapacitySchedulingForms.ProductCenterId_id = id
                CapacitySchedulingForms.save()
                messages.success(request, "Capacity Scheduling Create Successfully")
                return redirect('/productionplanning/copy-product-center/' + id)

            ProductCenterForms = ProductCenterForm(request.POST)
            if ProductCenterForms.is_valid():
                ProductCenterForms = ProductCenterForms.save()
                for x in CapacitySchedulingInstancrs:
                    dirs = {
                        'Date': x.Date,
                        'AvalCapOrDay': x.AvalCapOrDay,
                        'CapALlloctdTo': x.CapALlloctdTo,
                        'AlloctdCap': x.AlloctdCap,
                        'BalanceCap': x.BalanceCap,
                        'AvalMcOrResHour': x.AvalMcOrResHour,
                        'ReqdMcOrResHour': x.BalMcOrHour,
                        'StartTime': x.StartTime,
                        'EndTime': x.EndTime,
                        'NoOfMCAlloctd': x.NoOfMCAlloctd
                    }
                    form = CapacitySchedulingForm(data=dirs)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.ProductCenterId = ProductCenter.objects.get(id=ProductCenterForms.id)
                        form.save()
                        mass.append(True)
                    else:
                        mass.append(False)

                if len(mass) == mass.count(True):
                    messages.success(request, "{} to {} Copy Successfully".format(id, ProductCenterForms.id))
                    return redirect('/productionplanning/product-center/')
                else:
                    messages.error(request, "{} Copy Not Successfully".format(id))
                    return redirect('/productionplanning/product-center/')
            else:
                messages.error(request, "{} Copy Not Successfully".format(id))
                return redirect('/productionplanning/product-center/')
        else:
            messages.error(request, "{} Value Not Change".format(id))
            return redirect('/productionplanning/product-center/')
    else:
        copy_product_center_props['formset'] = formset
        copy_product_center_props['ProductCenter'] = ProductCenterForm(instance=ProductCenterInstancrs)
        copy_product_center_props["CapacitySchedulingForm"] = CapacitySchedulingForm()
        return render(request, 'PP/productcenter/update.html', context=copy_product_center_props)


def DeleteProductCenter(request, id):
    product_center = ProductCenter.objects.get(id=id)
    product_center.delete()
    messages.error(request, "{} Delete Successfully".format(id))
    return redirect('/productionplanning/product-center/')
