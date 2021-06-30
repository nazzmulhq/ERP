from django.db import models
from ..models.BOM import BOM
from ..models.ProductCenter import ProductCenter


class SemiFinishedAndFinished(models.Model):
    semifinishedandfinished = models.CharField(primary_key=True, editable=False, max_length=7, unique=True,
                                               verbose_name="Semi Finished ID")
    bom_ref = models.ForeignKey(BOM, related_name="bom", on_delete=models.SET_NULL, verbose_name="Bom ref.", blank=True, null=True)
    product_resp = models.CharField(max_length=32, blank=True, verbose_name="Product Resp.")
    inspection_ref = models.CharField(max_length=32, blank=True, verbose_name="Inspection Ref.")
    prod_center = models.ForeignKey(ProductCenter, related_name="product_center", on_delete=models.SET_NULL,
                                    verbose_name="Prod Center", null=True, blank=True)
    old_operation_list_ref = models.CharField(max_length=32, blank=True, verbose_name="Old Operation List Ref.")
    allowance = models.CharField(max_length=32, blank=True, verbose_name="Allowance")

    def save(self, *args, **kwargs):
        if not self.semifinishedandfinished:
            max = SemiFinishedAndFinished.objects.aggregate(
                id_max=models.Max('semifinishedandfinished'))['id_max']
            if max is not None:
                max = int(max[3:])
                max += 1
            else:
                max = 1
            max = "SFF{:04d}".format(max)
            self.semifinishedandfinished = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Semi Finished And Finished ID - {}".format(self.semifinishedandfinished)
