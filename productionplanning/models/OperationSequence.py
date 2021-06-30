from django.db import models
from productionplanning.models.OperationList import OperationList
from ..models.ProductCenter import ProductCenter


class OperationSequence(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=7)
    operation_list = models.ForeignKey(OperationList, on_delete=models.CASCADE)
    production_center = models.ForeignKey(ProductCenter,on_delete=models.CASCADE, null=True, blank=True, verbose_name='Production Center')
    os_date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    os_time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    operationSequence = models.CharField(max_length=32, verbose_name="Operation Sequence")
    baseunit = models.CharField(max_length=32, verbose_name="Base unit")
    reqdcapunit = models.CharField(max_length=32, verbose_name="Reqd Cap/Unit")
    standardtime = models.CharField(max_length=32, verbose_name="Standard time")
    allowancetime = models.CharField(max_length=32, verbose_name="Allowance time")
    totaltime = models.CharField(max_length=32, verbose_name="Total time", blank=True, null=True)
    componentsuser = models.CharField(max_length=32, verbose_name="Components user", blank=True, null=True)
    toolsrequired = models.CharField(max_length=32, verbose_name="Tools required", blank=True, null=True)
    inspectioncenter = models.CharField(max_length=32, verbose_name="Inspection Center")
    exceptionmsg = models.CharField(max_length=32, verbose_name="Exception msg", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = OperationSequence.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[2:])
                max += 1
            else:
                max = 1
            max = "OS{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)


