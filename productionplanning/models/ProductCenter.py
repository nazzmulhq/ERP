from django.db import models


class ProductCenter(models.Model):
    id = models.CharField(primary_key=True,
                          editable=False,
                          max_length=5,
                          unique=True,
                          verbose_name="Product Center ID")
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    user_data_entry_date_and_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Data Entry Date And Time")

    product_center_name = models.CharField(max_length=32, unique=True, verbose_name="Product Center Name")

    division = [
        ("", "---Select---"),
        ("Knit Fitter", "Knit-Fitter"),
        ("Knitting", "Knitting"),
        ("Batch", "Batch"),
        ("Dyeing", "Dyeing"),
        ("AOP", "AOP"),
        ("Finishing", "Finishing"),
        ("Other", "Other"),
    ]

    division = models.CharField(choices=division,
                                max_length=32,
                                default="---Select---",
                                verbose_name="Division")

    finalOutput = [
        ("", "---Select---"),
        ("M/C Set-Up", "M/C Set-Up"),
        ("Greige Fabric", "Greige Fabric"),
        ("RTD Batch", "RTD Batch"),
        ("Dyed Fabric", "Dyed Fabric"),
        ("AOP Fabric", "AOP Fabric"),
        ("Finished Fabric", "Finished Fabric"),
        ("Semi-Fin Product", "Semi-Fin Product"),
        ("Other", "Other"),
    ]

    final_output = models.CharField(max_length=32,
                                    choices=finalOutput,
                                    verbose_name="Final Output")
    m_by_c_or_tools = models.CharField(verbose_name="M / C or Tools",
                                       max_length=32)
    responsible_per = models.CharField(max_length=32,
                                       verbose_name="Responsible Per")
    unit = models.CharField(max_length=32, verbose_name="Unit")
    capacity_per_m_by_c = models.IntegerField(verbose_name="Capacity per M / C")
    NoOfMByC = models.IntegerField(verbose_name="No.of M / C")
    total_capacity_by_day = models.IntegerField(
        verbose_name="Total Capacity / Day",
        null=True,
        blank=True)
    m_by_c_per_operator = models.CharField(verbose_name="M / C per Operator", max_length=32,
                                           null=True,
                                           blank=True)
    total_opeartor_by_day = models.IntegerField(
        verbose_name="Total Opeartor / Day",
        null=True,
        blank=True)
    exception_msg = models.CharField(verbose_name="Exception Msg",
                                     max_length=32,
                                     null=True,
                                     blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = ProductCenter.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "W{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product_center_name)

    class Meta:
        ordering = ['-date', '-time']


class CapacityScheduling(models.Model):
    ProductCenterId = models.ForeignKey(ProductCenter, on_delete=models.CASCADE, related_name="ProductCenter")
    id = models.CharField(
        max_length=32,
        primary_key=True,
        editable=False,
        unique=True,
        verbose_name="Capacity Schedulling ID")
    cs_date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    cs_time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")

    Date = models.DateField(verbose_name="Date")
    AvalCapOrDay = models.IntegerField(default=0, blank=True, null=True,
                                       verbose_name="AVAL CAP / DAY")
    CapALlloctdTo = models.CharField(max_length=10, blank=True, null=True,
                                     verbose_name="CAP ALLOCTD TO")
    AlloctdCap = models.CharField(blank=True, null=True, verbose_name="ALLOCTD CAP", max_length=30)
    BalanceCap = models.CharField(blank=True, null=True, verbose_name="BALANCE CAP", max_length=30)
    AvalMcOrResHour = models.CharField(max_length=35, blank=True, null=True,
                                       verbose_name="AVAL MC/RES HOUR")
    ReqdMcOrResHour = models.CharField(max_length=32, blank=True, null=True,
                                       verbose_name="REQD MC/RES HOUR")
    BalMcOrHour = models.CharField( blank=True, null=True, max_length=32,
                                   verbose_name="BAL MC/RES HOUR")
    StartTime = models.TimeField(blank=True, null=True, verbose_name="START TIME")
    EndTime = models.TimeField(blank=True, null=True, verbose_name="END TIME")
    NoOfMCAlloctd = models.IntegerField(default=0, blank=True, null=True,
                                        verbose_name="NO.OF MC ALLOCTD")

    def save(self, *args, **kwargs):
        if not self.id:
            max = CapacityScheduling.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[2:])
                max += 1
            else:
                max = 1
            max = "CS{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Capacity Scheduling ID - {}".format(self.id)
