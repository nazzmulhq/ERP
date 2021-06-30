from django.contrib import admin
from productionplanning.models.Product import Product
from productionplanning.models.SemiFinishedAndFinished import SemiFinishedAndFinished
from productionplanning.models.BomAndRawMaterial import BomAndRowMaterial
from productionplanning.models.FinishedAndOther import FinishedAndOther
from productionplanning.models.RawMaterial import RawMaterial
from productionplanning.models.SemiFinished import SemiFinished
from productionplanning.models.Finished import Finished
from productionplanning.models.OtherProduct import Other
from productionplanning.models.BOM import BOM
from productionplanning.models.ProductCenter import ProductCenter, CapacityScheduling
from productionplanning.models.OperationList import OperationList
from productionplanning.models.OperationSequence import OperationSequence
from productionplanning.models.CRP import CRP
from productionplanning.models.MRP import MRP
from productionplanning.models.MRP import MRPGeneralData
from productionplanning.models.SubmissionAndApproval import SubmissionAndApproval

# Register your models here.

admin.site.register(Product)
admin.site.register(SemiFinishedAndFinished)
admin.site.register(BomAndRowMaterial)
admin.site.register(FinishedAndOther)
admin.site.register(RawMaterial)
admin.site.register(SemiFinished)
admin.site.register(Finished)
admin.site.register(Other)
admin.site.register(BOM)
admin.site.register(OperationSequence)
admin.site.register(ProductCenter)
admin.site.register(CapacityScheduling)
admin.site.register(OperationList)
admin.site.register(CRP)
admin.site.register(MRP)
admin.site.register(MRPGeneralData)
admin.site.register(SubmissionAndApproval)