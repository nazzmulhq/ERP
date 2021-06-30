from django.db import models
from .Product import Product
from .SemiFinishedAndFinished import SemiFinishedAndFinished
from .Finished import Finished
from .ProductCenter import ProductCenter


class SemiFinished(Product, SemiFinishedAndFinished):
    Finished = models.ForeignKey(Finished, on_delete=models.SET_NULL, null=True, blank=True,
                                             related_name="semifinishedfinished")


    id = models.CharField(primary_key=True, editable=False, max_length=7, unique=True, verbose_name="Semi Finished ID")

    Category = [
        ("", "---Select---"),
        ("Dyed Yarn", "Dyed Yarn"),
        ("Greige Fabric", "Greige Fabric"),
        ("RTD Fabric", "RTD Fabric"),
        ("RTP Fabric", "RTP Fabric"),
        ('Other', "Other")

    ]
    product_category = models.CharField(choices=Category, max_length=32, default="---Select---",
                                        verbose_name="Product Category")
    time_0f_pur_or_prd = models.TimeField(max_length=32, verbose_name="Date Of Pur/Prd", null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.id:
            max = SemiFinished.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[2:])
                max += 1
            else:
                max = 1
            max = "SF{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Semi-Finished ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
