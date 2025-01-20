from django.contrib import admin

from retailing.models import Supplier


@admin.action
def clean_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # Представление модели Supplier в admin панели
    list_display = ('id', 'title', 'debt', 'created_time', 'level')
    fields = [('title', 'level'), ('contacts', 'city'), 'products', 'up_supplier', 'debt', 'created_time']
    list_filter = ('city',)
    actions = [clean_debt, ]
