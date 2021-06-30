from django.db import models

from productionplanning.models.OperationList import OperationList


class FinishedAndOther(models.Model):
    operations_list = models.ForeignKey(OperationList, related_name="operations_list", on_delete=models.SET_NULL, null=True, blank=True)
    finishedandother = models.CharField(primary_key=True, editable=False, max_length=6, unique=True,
                                        verbose_name="Finished And Other ID")
    Category = [
        ("", "---Select---"),
        ("Dyed Yarn RTD", "Dyed Yarn RTD"),
        ("Dyed Fabric RTD", "Dyed Fabric RTD"),
        ("AOP Fabric RTD", "AOP Fabric RTD"),
        ('Other', "Other")

    ]
    product_category = models.CharField(choices=Category, max_length=32, default="---Select---",
                                        verbose_name="Product Category")
    lab_ref = models.CharField(max_length=32, blank=True)
    r_and_d_ref = models.CharField(max_length=32, blank=True)
    packing_instruction = models.CharField(max_length=32, blank=True)

    def save(self, *args, **kwargs):
        if not self.finishedandother:
            max = FinishedAndOther.objects.aggregate(
                id_max=models.Max('finishedandother'))['id_max']
            if max is not None:
                max = int(max[3:])
                max += 1
            else:
                max = 1
            max = "FO{:04d}".format(max)
            self.finishedandother = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Finished And Other ID - {}".format(self.finishedandother)
