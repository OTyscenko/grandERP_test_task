from django.contrib import admin

from .models import ExpenseType, Suplier, Expense

admin.site.register(ExpenseType)
admin.site.register(Suplier)
# admin.site.register(Expense)

class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ('document_no', 'date', 'summed')

admin.site.register(Expense, ExpenseAdmin)