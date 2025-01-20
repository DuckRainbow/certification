from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Проверка на активность сотрудника"""

    def has_permission(self, request, view):
        return request.user.is_active == True
