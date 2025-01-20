from django.contrib import admin

from retailing.models import Supplier, Contact, Product


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Представление модели Contact в admin панели
    list_display = ('id', 'email', 'country', 'city')
    fields = ['email', 'country', 'city', ('street', 'building')]
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Представление модели Product в admin панели
    list_display = ('id', 'title', 'type', 'date_of_release')
