from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsActive

from retailing.models import Contact, Product, Supplier
from retailing.paginators import PagePagination
from retailing.serializers import SupplierSerializer, SupplierCreateSerializer, SupplierUpdateSerializer, \
    ContactSerializer, ProductSerializer


class ContactCreateAPIView(CreateAPIView):
    """Создание объекта контакта"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticated, IsActive)


class ContactListAPIView(ListAPIView):
    """Контроллер для просмотра списка всех контактов"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        "country",
        "city",
        "email",
        "street",
    )
    permission_classes = (IsAuthenticated, IsActive)
    pagination_class = PagePagination


class ContactRetrieveAPIView(RetrieveAPIView):
    """Контроллер для просмотра контакта"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsActive)


class ContactUpdateAPIView(UpdateAPIView):
    """Контроллер для изменения контакта"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsActive)


class ContactDestroyAPIView(DestroyAPIView):
    """Контроллер для удаления контакта"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsActive)


class ProductCreateAPIView(CreateAPIView):
    """Создание объекта продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, IsActive)


class ProductListAPIView(ListAPIView):
    """Контроллер для просмотра списка всех продуктов"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        "title",
        "type",
        "date_of_release",
    )
    permission_classes = (IsAuthenticated, IsActive)
    pagination_class = PagePagination


class ProductRetrieveAPIView(RetrieveAPIView):
    """Контроллер для просмотра продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive)


class ProductUpdateAPIView(UpdateAPIView):
    """Контроллер для изменения продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive)


class ProductDestroyAPIView(DestroyAPIView):
    """Контроллер для удаления продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsActive)


class SupplierCreateAPIView(CreateAPIView):
    """Создание объекта продукта"""
    serializer_class = SupplierCreateSerializer
    queryset = Supplier.objects.all()
    permission_classes = (IsAuthenticated, IsActive)


class SupplierListAPIView(ListAPIView):
    """Контроллер для просмотра списка всех продуктов"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        "title",
        "contacts",
        "products",
        "supplier",
        "created_time",
        "contacts.country"
    )
    permission_classes = (IsAuthenticated, IsActive)
    pagination_class = PagePagination


class SupplierRetrieveAPIView(RetrieveAPIView):
    """Контроллер для просмотра продукта"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, IsActive)


class SupplierUpdateAPIView(UpdateAPIView):
    """Контроллер для изменения продукта"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer
    permission_classes = (IsAuthenticated, IsActive)


class SupplierDestroyAPIView(DestroyAPIView):
    """Контроллер для удаления продукта"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, IsActive)
