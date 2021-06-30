"""rootfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from productionplanning.views import RawMaterialViews
from productionplanning.views import SemiFinishedViews
from productionplanning.views import FinishedViews
from productionplanning.views import OtherViews
from productionplanning.views import OperationListViews
from productionplanning.views import BOMViews
from productionplanning.views import ProductCenterViews
from productionplanning.views import MRPViews
from productionplanning.views import CRPViews
from productionplanning.views import SubmissionAndApprovalViews

app_name = 'productionplanning'

urlpatterns = [

    # RawMaterialViews

    path('raw-material/', RawMaterialViews.ListRawMaterial, name="ListRawMaterial"),
    path('filtering-raw-material/', RawMaterialViews.FilterRawMaterial, name="FilterRawMaterial"),
    path('add-raw-material/', RawMaterialViews.PostRawMaterial, name="AddRawMaterial"),
    path('view-raw-material/<slug:id>/', RawMaterialViews.ViewRawMaterial, name="ViewRawMaterial"),
    path('update-raw-material/<slug:id>/', RawMaterialViews.UpdateRawMaterial, name="UpdateRawMaterial"),
    path('copy-raw-material/<slug:id>/', RawMaterialViews.CopyRawMaterial, name="CopyRawMaterial"),
    path('delete-raw-material/<slug:id>/', RawMaterialViews.DeleteRawMaterial, name="DeleteRawMaterial"),

    # SemiFinishedViews

    path('semi-finished/', SemiFinishedViews.ListSemiFinished, name="ListSemiFinished"),
    path('filtering-semi-finished/', SemiFinishedViews.FilterSemiFinished, name="FilterSemiFinished"),
    path('add-semi-finished/', SemiFinishedViews.PostSemiFinished, name="AddSemiFinished"),
    path('view-semi-finished/<slug:id>/', SemiFinishedViews.ViewSemiFinished, name="ViewSemiFinished"),
    path('update-semi-finished/<slug:id>/', SemiFinishedViews.UpdateSemiFinished, name="UpdateSemiFinished"),
    path('copy-semi-finished/<slug:id>/', SemiFinishedViews.CopySemiFinished, name="CopySemiFinished"),
    path('delete-semi-finished/<slug:id>/', SemiFinishedViews.DeleteSemiFinished, name="DeleteSemiFinished"),

    # FinishedViews

    path('finished/', FinishedViews.ListFinished, name="ListFinished"),
    path('filtering-finished/', FinishedViews.FilterFinished, name="FilterFinished"),
    path('add-finished/', FinishedViews.PostFinished, name="AddFinished"),
    path('view-finished/<slug:id>/', FinishedViews.ViewFinished, name="ViewFinished"),
    path('update-finished/<slug:id>/', FinishedViews.UpdateFinished, name="UpdateFinished"),
    path('copy-finished/<slug:id>/', FinishedViews.CopyFinished, name="CopyFinished"),
    path('delete-finished/<slug:id>/', FinishedViews.DeleteFinished, name="DeleteFinished"),

    # OtherViews

    path('other/', OtherViews.ListOther, name="ListOther"),
    path('filtering-other/', OtherViews.FilterOtherProduct, name="FilterOtherProduct"),
    path('add-other/', OtherViews.PostOther, name="AddOther"),
    path('view-other/<slug:id>/', OtherViews.ViewOther, name="ViewOther"),
    path('update-other/<slug:id>/', OtherViews.UpdateOther, name="UpdateOther"),
    path('copy-other/<slug:id>/', OtherViews.CopyOther, name="CopyOther"),
    path('delete-other/<slug:id>/', OtherViews.DeleteOther, name="DeleteOther"),

    # OperationListViews

    path('operation-list/', OperationListViews.ListOperationList, name="ListOperationList"),
    path('filtering-operation-list/', OperationListViews.FilterOperationList, name="FilterOperationList"),
    path('add-operation-list/', OperationListViews.PostOperationList, name="AddOperationList"),
    path('add-operation-sequence/<slug:id>/', OperationListViews.PostOperationSequence, name="PostOperationSequence"),
    path('add2-operation-sequence/<slug:id>/', OperationListViews.PostFinishOperationSequence, name="PostFinishOperationSequence"),
    path('view-operation-list/<slug:id>/', OperationListViews.ViewOperationList, name="ViewOperationList"),
    path('update-operation-list/<slug:id>/', OperationListViews.UpdateOperationList, name="UpdateOperationList"),
    path('copy-operation-list/<slug:id>/', OperationListViews.CopyOperationList, name="CopyOperationList"),
    path('update-operation-sequence/<slug:id>/', OperationListViews.UpdateOperationSequence,
         name="UpdateOperationSequence"),
    path('delete-operation-list/<slug:id>/', OperationListViews.DeleteOperationList, name="DeleteOperationList"),

    # BOMViews

    path('bom/', BOMViews.ListBOM, name="ListBOM"),
    path('filtering-bom/', BOMViews.FilterBOM, name="FilterBOM"),
    path('add-bom/', BOMViews.PostBOM, name="AddBOM"),
    path('add-raw-in-bom/<slug:id>/', BOMViews.RawInBOM, name="RawInBOM"),
    path('add-finishe-raw-in-bom/<slug:id>/', BOMViews.FinishedRawInBOM, name="FinishedRawInBOM"),
    path('view-bom/<slug:id>/', BOMViews.ViewBOM, name="ViewBOM"),
    path('update-bom/<slug:id>/', BOMViews.UpdateBOM, name="UpdateBOM"),
    path('update-bom-row-material/<slug:id>/', BOMViews.UpdateBomAndRowMaterial,
         name="UpdateBomAndRowMaterial"),
    path('copy-bom/<slug:id>/', BOMViews.CopyBOM, name="CopyBOM"),
    path('delete-bom/<slug:id>/', BOMViews.DeleteBOM, name="DeleteBOM"),

    # ProductCenterViews

    path('product-center/', ProductCenterViews.ListProductCenter, name="ListProductCenter"),
    path('filtering-product-center/', ProductCenterViews.FilterProductCenter, name="FilterProductCenter"),
    path('add-product-center/', ProductCenterViews.PostProductCenter, name="AddProductCenter"),
    path('view-product-center/<slug:id>/', ProductCenterViews.ViewProductCenter, name="ViewProductCenter"),
    path('update-product-center/<slug:id>/', ProductCenterViews.UpdateProductCenter, name="UpdateProductCenter"),
    path('copy-product-center/<slug:id>/', ProductCenterViews.CopyProductCenter, name="CopyProductCenter"),
    path('update-capacity-scheduling/<slug:id>/', ProductCenterViews.UpdateCapacityScheduling,
         name="UpdateCapacityScheduling"),
    path('delete-product-center/<slug:id>/', ProductCenterViews.DeleteProductCenter, name="DeleteProductCenter"),

    # CRP Views
    path('crp/', CRPViews.ListCRP, name="ListCRP"),
    path('filtering-crp/', CRPViews.FilterCRP, name="FilterCRP"),
    path('add-crp/', CRPViews.PostCRP, name="AddCRP"),
    path('add-crps/<slug:id>', CRPViews.AddCRP, name="CRP"),
    path("view-crp/<slug:id>/", CRPViews.ViewCRP, name='ViewCRP'),
    path("update-crp/<slug:id>/", CRPViews.UpdateCRP, name='UpdateCRP'),
    path("copy-crp/<slug:id>/", CRPViews.CopyCRP, name='CopyCRP'),
    path("delete-crp/<slug:id>/", CRPViews.DeleteCRP, name='DeleteCRP'),

    # MRP Views

    path('mrp/', MRPViews.ListMRP, name="ListMRP"),
    path('filtering-mrp/', MRPViews.FilterMRP, name="FilterMRP"),
    path("add-mrp-general-data/", MRPViews.PostMRPGeneral, name='PostMRPGeneral'),
    path("add-mrp/<slug:id>/", MRPViews.PostMRP, name='PostMRP'),
    path("view-mrp/<slug:id>/", MRPViews.PostMRPView, name='PostMRPView'),
    path("view-mrps/<slug:id>/", MRPViews.ViewMRP, name='ViewMRP'),
    path("update-mrp/<slug:id>/", MRPViews.UpdateMRP, name='UpdateMRP'),
    path("copy-mrp/<slug:id>/", MRPViews.CopyMRP, name='CopyMRP'),
    path("delete-mrp/<slug:id>/", MRPViews.DeleteMRP, name='DeleteMRP'),

    # Submission And Approval
    path('submission-and-approval/', SubmissionAndApprovalViews.ListSubmissionAndApproval,
         name="ListSubmissionAndApproval"),
    path('filtering-submission-and-approval/', SubmissionAndApprovalViews.FilterSubmissionAndApproval,
         name="FilterSubmissionAndApproval"),
    path('add-submission-and-approval/', SubmissionAndApprovalViews.PostSubmissionAndApproval,
         name="PostSubmissionAndApproval"),
    path('view-submission-and-approval/<slug:id>/', SubmissionAndApprovalViews.ViewSubmissionAndApproval,
         name="ViewSubmissionAndApproval"),
    path('update-submission-and-approval/<slug:id>/', SubmissionAndApprovalViews.UpdateSubmissionAndApproval,
         name="UpdateSubmissionAndApproval"),
    path('copy-submission-and-approval/<slug:id>/', SubmissionAndApprovalViews.CopySubmissionAndApproval,
         name="CopySubmissionAndApproval"),
    path('delete-submission-and-approval/<slug:id>/', SubmissionAndApprovalViews.DeleteSubmissionAndApproval,
         name="DeleteSubmissionAndApproval"),

]
