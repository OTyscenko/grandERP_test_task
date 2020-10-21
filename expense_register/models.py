from django.db import models

# Create your models here.

class ExpenseType(models.Model):
    type_name = models.CharField(max_length=50)

class Suplier(models.Model):
    type_name = models.CharField(max_length=50)

class Expense(models.Model):
    date = models.DateTimeField()
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    document_no = models.CharField(max_length=50)
    summed = models.DecimalField(max_digits=20, decimal_places=2, min_value=0.01)
