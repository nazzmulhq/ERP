from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    # General for RawMaterials
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="user",
                             related_name="UserRelated",
                             related_query_name="UserQuery", null=True, blank=True)
    product = models.CharField(primary_key=True, unique=True, editable=False, max_length=5)
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")

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

    priceunit = [
        ("", "---Select---"),
        ("BD", "Tk"),
        ("Dollar ", "Dollar"),
        ("Pound ", "Pound"),
        ("Euro", "Euro"),
    ]
    price_unit = models.CharField(choices=priceunit, max_length=32, default="---Select---", blank=True,
                                  verbose_name="Price/Unit")
    price = models.CharField(max_length=32, blank=True, verbose_name="Price")

    # Purchase Sales Marketing for RawMaterials
    dateOfPurPrd = [
        ("", "---Select---"),
        ("Purchase Date", "Purchase Date"),
        ("Production Date", "Production Date"),
    ]
    pur_or_prd = models.CharField(choices=dateOfPurPrd, max_length=32,
                                  verbose_name="Pur/Prd")
    date_0f_pur_or_prd = models.DateField(max_length=32, verbose_name="Date Of Pur/Prd")
    Source = [
        ("", "---Select---"),
        ("In House", "In House"),
        ("Local Purchase", "Local Purchase"),
        ("Foreign Purchase", "Foreign Purchase"),
        ('Other', "Other")
    ]
    source = models.CharField(choices=Source, max_length=32, verbose_name="Source")
    previous_ref = models.CharField(max_length=32, verbose_name="Previous Ref.")
    lead_time = models.CharField(max_length=32, blank=True, verbose_name="Lead Time")
    responsible_dept = models.CharField(max_length=32, blank=True, verbose_name="Responsible Dept.")
    usage_ref = models.CharField(max_length=32, blank=True, verbose_name="Usage Ref.")

    # Factory for RawMaterials
    mrp_responsible = models.CharField(max_length=32, verbose_name="MRP Responsible")
    lot_size = models.CharField(max_length=32, blank=True, verbose_name="Lot Size")

    # WareHouse for RawMaterials
    warehouse_location = models.CharField(max_length=32, verbose_name="Warehouse Location")
    shipping_unit = models.CharField(max_length=32, blank=True, null=True, verbose_name="Shipping Unit")
    qty_or_unit = models.CharField(max_length=32, blank=True, null=True, verbose_name="Qty/Unit")
    gross_wt = models.CharField(max_length=32, blank=True, null=True, verbose_name="Gross Wt.")
    net_wt = models.CharField(max_length=32, blank=True, null=True, verbose_name="Net Wt.")
    storage_instruction = models.CharField(max_length=32, blank=True, null=True, verbose_name="Storage Instruction")

    def save(self, *args, **kwargs):
        if not self.product:
            max = Product.objects.aggregate(
                id_max=models.Max('product'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "P{:04d}".format(max)
            self.product = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Product ID - {}".format(self.product)
