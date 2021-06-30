from django.db import models


class OperationList(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=7)
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    dataOfcreation = models.DateField(max_length=10, verbose_name="Date of creation")
    Usage = [
        ("Production", "Production"),
        ("Development", "Development"),
        ("Costing", "Costing"),
        ("Other", "Other")
    ]
    usage = models.CharField(choices=Usage, max_length=32, verbose_name="Usage")
    productioncategory = [
        ("Finished Product", "Finished Product"),
        ("WIP", "WIP"),
        ("Other", "Other"),
    ]
    productioncategory = models.CharField(choices=productioncategory, max_length=32, verbose_name="Production Category")
    productdescription = models.CharField(max_length=32, verbose_name="Product Description", blank=True, null=True)
    responsibledept = models.CharField(max_length=32, verbose_name="Responsible Dept")
    previousref = models.CharField(max_length=32, verbose_name="Previous Ref.", blank=True, null=True)


    orderref = models.CharField(max_length=32, verbose_name="Order Ref", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            max = OperationList.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "O{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Operation List ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']