from django.db import models
from .Finished import Finished
from .OperationList import OperationList


class CRPTrack(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=10)
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    finished = models.ForeignKey(Finished, on_delete=models.CASCADE)
    operationlist = models.CharField(max_length=32, null=True, blank=True)
    product_description = models.CharField(max_length=64, null=True, blank=True)
    order_ref = models.CharField(max_length=64, null=True, blank=True)
    order_qty = models.CharField(max_length=64, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = CRPTrack.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[3:])
                max += 1
            else:
                max = 1
            max = "CRP{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']


class CRP(models.Model):
    id = models.CharField(
        max_length=32,
        primary_key=True,
        editable=False,
        unique=True)
    crp_date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    crp_time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    crp_track = models.ForeignKey(CRPTrack, on_delete=models.CASCADE)
    # operation list
    operationSequence = models.CharField(max_length=32, verbose_name="Operation Sequence")
    productioncneter = models.CharField(max_length=32, verbose_name="Production Cneter")
    AvalStartDate = models.CharField(max_length=32, verbose_name='Aval Start Date', null=True,blank=True)
    StartDate = models.DateField(null=True, verbose_name='START DATE', blank=True)
    reqdcapunit = models.CharField(max_length=32, verbose_name="Reqd Cap/Unit", blank=True)
    ReqdMcHrByUnit = models.CharField(max_length=32, blank=True, null=True,
                                         verbose_name="Reqd MC Hr/Unit",)
    # production center

    AvalStartTime = models.CharField(max_length=32, verbose_name='Aval Start Time', null=True, blank=True)
    AvalMcHrOrDay = models.CharField(max_length=32, blank=True, null=True,
                                     verbose_name="AVAL MC Hr/Day")
    NoOfMCByResAval = models.CharField(max_length=32, verbose_name="No of MC/RES Aval", null=True, blank=True)
    AvalCAPByDay = models.CharField(verbose_name="AVAL CAP/DAY", null=True, max_length=32, blank=True)

    # crp

    ReqdCAPByDay = models.CharField(verbose_name="REQD CAP / DAY", null=True, max_length=32, blank=True)
    ReqdMcHour = models.CharField(verbose_name="REQD MC Hour", null=True, max_length=32, blank=True)
    StartTime = models.TimeField(verbose_name="START TIME", null=True, blank=True)
    EndTime = models.TimeField(verbose_name="End Time", null=True, blank=True)
    EndDate = models.DateField(verbose_name="END DATE", null=True, blank=True)
    NoOfMcByRes = models.CharField(verbose_name="No. Of MC/RES", null=True, max_length=32, blank=True)
    mc_id_no = models.CharField(verbose_name='MC ID / NO', null=True, max_length=32, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = CRP.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[4:])
                max += 1
            else:
                max = 1
            max = "CRPS{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)



