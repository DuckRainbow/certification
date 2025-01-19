from django.contrib import admin

from retailing.models import Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contacts', 'products', 'supplier', 'debt', 'created_time', 'level')
    list_filter = ('contact.city',)
