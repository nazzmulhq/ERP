from django.db import models
from .Product import Product
from .SemiFinishedAndFinished import SemiFinishedAndFinished
from .FinishedAndOther import FinishedAndOther
from .BOM import BOM


class Other(Product, SemiFinishedAndFinished, FinishedAndOther):
    # General for Finished
    id = models.CharField(primary_key=True, editable=False, max_length=5, unique=True)


    def save(self, *args, **kwargs):
        if not self.id:
            max = Other.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "X{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Other ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
