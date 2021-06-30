from django.db import models
from .Product import Product


class RawMaterial(Product):
    Category = [
        ("", "---Select---"),
        ("Yarn", "Yarn"),
        ("Dyes", "Dyes"),
        ("Chemicals", "Chemicals"),
        ('Other', "Other")

    ]
    product_category = models.CharField(choices=Category, max_length=32, default="---Select---",
                                        verbose_name="Product Category")
    time_0f_pur_or_prd = models.TimeField(max_length=32, verbose_name="Date Of Pur/Prd", null=True, blank=True)

    id = models.CharField(primary_key=True, editable=False, max_length=5, unique=True, verbose_name="Raw Materials ID")

    def save(self, *args, **kwargs):
        if not self.id:
            max = RawMaterial.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "R{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Raw Materials ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
