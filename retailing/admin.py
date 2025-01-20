from django.contrib import admin

from retailing.models import Supplier


def clean_debt(pk):
    supplier = Supplier.objects.filter(id=pk)
    supplier.debt = 0
    supplier.save()


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # Представление модели Supplier в admin панели
    list_display = ('id', 'title', 'debt', 'created_time', 'level')
    fields = [('id', 'title', 'level'), 'contacts', 'products', 'supplier', 'debt', 'created_time']
    list_filter = ('contact.city',)
    actions = [clean_debt, ]
