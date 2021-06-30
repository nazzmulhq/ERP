from django.db import models
from .OperationList import OperationList
from .Product import Product
from .SemiFinishedAndFinished import SemiFinishedAndFinished
from .FinishedAndOther import FinishedAndOther


class Finished(Product, SemiFinishedAndFinished, FinishedAndOther):
    id = models.CharField(primary_key=True, editable=False, max_length=5, unique=True, verbose_name="Finished ID")

    def save(self, *args, **kwargs):
        if not self.id:
            max = Finished.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[1:])
                max += 1
            else:
                max = 1
            max = "F{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Finished ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
