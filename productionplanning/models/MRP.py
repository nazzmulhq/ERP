from django.db import models


class MRPGeneralData(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=10)
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    data = models.DateField(verbose_name="Date")
    order_ref = models.CharField(max_length=32, verbose_name='ORDER REF')
    Mrp_purpose = [
        ("", "---Select---"),
        ("Make-To-Order", "Make-To-Order"),
        ("Make-To-Stock", "Make-To-Stock"),
        ("Consumables", "Consumables"),
        ("Sub-Contact-Inside", "Sub-Contact-Inside"),
        ("Sub-Contact-Outside", "Sub-Contact-Outside"),
    ]
    mrp_purpose = models.CharField(choices=Mrp_purpose, max_length=32, verbose_name='MRP PURPOSE')
    ResponsibleDept = [
        ("", "---Select---"),
        ("Planning Dept", "Planning Dept"),
        ("Dept 2", "Dept 2"),
        ("Dept 3", "Dept 3"),
        ("Dept 4", "Dept 4"),
        ("Dept 5", "Dept 5"),
    ]
    responsible_dept = models.CharField(choices=ResponsibleDept, max_length=32, verbose_name='Responsible Dept')
    final_prod_no = models.CharField(max_length=32, verbose_name='FINAL PROD NO')
    final_prod_des = models.CharField(max_length=32, verbose_name='FINAL PROD DES')
    bom_ref_no = models.CharField(max_length=32, verbose_name='BOM REF NO')

    def save(self, *args, **kwargs):
        if not self.id:
            max = MRPGeneralData.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[4:])
                max += 1
            else:
                max = 1
            max = "MRP{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "MRP General Data - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']


class MRP(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=10)
    mrp_date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    mrp_time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    mrp_general_data = models.ForeignKey(MRPGeneralData, on_delete=models.CASCADE)
    raw_id = models.CharField(verbose_name='RAW NO', max_length=32, null=True, blank=True)
    product_description = models.CharField(verbose_name='RAW DESCRIPTION', max_length=32, null=True, blank=True)
    unit = models.CharField(verbose_name='UNIT', max_length=32, null=True, blank=True)
    qty_required = models.CharField(verbose_name='REQUIRED QTY', max_length=32, null=True, blank=True)
    total_reqd_qty = models.CharField(verbose_name='TOTAL REQD QTY', max_length=32, null=True, blank=True)
    required_date = models.DateField(verbose_name='REQUIRED DATE', max_length=32, null=True, blank=True)

    Source = [
        ("", "---Select---"),
        ("In House Production", "In-House Production"),
        ("Out Side", "Out Side"),
        ("In Store", "In-Store"),

    ]
    source = models.CharField(choices=Source, max_length=32, verbose_name="Source", null=True, blank=True)
    source_name = models.CharField(verbose_name='SOURCE NAME', max_length=32, null=True, blank=True)
    action_required = [
        ("", "---Select---"),
        ("Place Production Order", "Place Production Order"),
        ("Place Purchase Order", "Place Purchase Order"),
        ("Place Requisition Slip", "Place Requisition Slip"),
    ]
    action_required = models.CharField(choices=action_required, verbose_name='ACTION REQUIRED', max_length=32,
                                       null=True, blank=True)
    status = models.CharField(verbose_name='Status', max_length=32, null=True, blank=True)
    time_to_get = models.CharField(verbose_name='TIME TO GET', max_length=32, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = MRP.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[4:])
                max += 1
            else:
                max = 1
            max = "MRPS{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "MRP General Data - {}".format(self.id)

