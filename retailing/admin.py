from django.contrib import admin

from retailing.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # Представление модели Supplier в admin панели
    list_display = ('id', 'title', 'contacts', 'products', 'supplier', 'debt', 'created_time', 'level')
    list_filter = ('contact.city',)
