from django.db import models
from .RawMaterial import RawMaterial
from .BOM import BOM


class BomAndRowMaterial(models.Model):
    raw_material = models.CharField(max_length=10, verbose_name='Raw Material ID',null=True,)
    bom = models.ForeignKey(BOM, on_delete=models.CASCADE)
    Category = [
        ("", "---Select---"),
        ("Yarn", "Yarn"),
        ("Dyes", "Dyes"),
        ("Chemicals", "Chemicals"),
        ('Other', "Other")
    ]
    product_category = models.CharField(choices=Category, max_length=32, default="---Select---",
                                        verbose_name="Product Category")
    product_description = models.CharField(max_length=32, verbose_name="Product Description")
    unit = [
        ("", "---Select---"),
        ("KG", "KG"),
        ("LB", "LB"),
        ("CM", "CM"),
        ("L", "L"),
        ("meter", "Meter"),
        ("gm", "GM"),
        ("feet", "Feet"),
        ("inch", "Inch"),
        ("yard", "Yard"),
    ]
    unit = models.CharField(choices=unit, max_length=32, default="---Select---", blank=True, verbose_name="Unit")
    qty_required = models.CharField(max_length=32, verbose_name="Qty Required")
    assigned_stroe = models.CharField(max_length=32, null=True, blank=True, verbose_name="Assigned Stroe")
    status = models.CharField(max_length=32, null=True, blank=True, verbose_name="Status")

    def __str__(self):
        return str(self.bom)
