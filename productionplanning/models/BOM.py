from django.db import models
from .RawMaterial import RawMaterial


class BOM(models.Model):
    # productcenter = models.ForeignKey(ProductCenter, on_delete=models.SET_NULL, related_name="productcenter", null=True,
    #                                   blank=True)
    id = models.CharField(primary_key=True, editable=False, max_length=5, unique=True, verbose_name="BOM ID")
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    purpose = [
        ("", "---Select---"),
        ("Production", "Production"),
        ("Development", "Development"),
        ("Other", "Other"),
    ]
    purpose_of_bom = models.CharField(choices=purpose, max_length=32, default="---Select---",
                                      verbose_name="Purpose Of BOM")
    final_product = models.CharField(max_length=32, verbose_name="Final Product")
    unit_of_meas = models.CharField(max_length=32, verbose_name="Unit of Meas")
    order_ref = models.CharField(max_length=32, verbose_name="Order Ref.")
    responsible_dept = models.CharField(max_length=32, verbose_name="Responsible Dept.")
    options_or_old_bom = models.CharField(max_length=32, null=True, blank=True, verbose_name="Options/Old BOM")
    valid_from = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Valid From")
    valid_to = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Valid To")
    labref = models.CharField(max_length=32, null=True, blank=True, verbose_name="Lab Ref. No")

    def save(self, *args, **kwargs):
        if not self.id:
            max = BOM.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "B{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "BOM ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
