from decimal import Decimal
from django.db import models

# Create your models here.

class ExpenseType(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name


class Suplier(models.Model):
    supplier_name = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier_name


class Expense(models.Model):
    date = models.DateTimeField()
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    document_no = models.CharField(max_length=50)
    summed = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.document_no}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(summed__gt=Decimal('0.01')),
                name='summed_gt_0.1',
            )
        ]
