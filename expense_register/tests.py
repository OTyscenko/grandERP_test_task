from django.test import TestCase
from .models import ExpenseType, Suplier, Expense
from django.db.utils import IntegrityError

class ExpenseModelTest(TestCase):
    date = '2014-01-01'
    type = 'Telefonas'
    suplier = 'Omnitel'
    document_no = 'telefono saskaita FSD785466'
    summed = '158.21'

    def test_proper_data(self):
        expense_type = ExpenseType.objects.create(type_name=self.type)
        suplier = Suplier.objects.create(supplier_name=self.suplier)
        Expense.objects.create(
            date=self.date,
            type=expense_type,
            suplier=suplier,
            document_no=self.document_no,
            summed=self.summed
        )
        expense = Expense.objects.all()
        self.assertEqual(expense.count(), 1)

    def test_zero_sum(self):
        expense_type = ExpenseType.objects.create(type_name=self.type)
        suplier = Suplier.objects.create(supplier_name=self.suplier)
        with self.assertRaises(IntegrityError):
            Expense.objects.create(
                date=self.date,
                type=expense_type,
                suplier=suplier,
                document_no=self.document_no,
                summed=0
            )