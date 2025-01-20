from django.contrib import admin

from users.models import User


@admin.register(User)
class SupplierAdmin(admin.ModelAdmin):
    # Представление модели Supplier в admin панели
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_num', 'is_active' )
