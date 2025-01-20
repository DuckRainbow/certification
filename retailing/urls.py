from django.urls import path
from rest_framework.routers import DefaultRouter

from retailing.apps import RetailingConfig
from retailing.views import (
    SupplierListAPIView,
    SupplierCreateAPIView,
    SupplierRetrieveAPIView,
    SupplierUpdateAPIView,
    SupplierDestroyAPIView,
    ContactListAPIView,
    ContactCreateAPIView,
    ContactRetrieveAPIView,
    ContactUpdateAPIView,
    ContactDestroyAPIView,
    ProductListAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)

app_name = RetailingConfig.name

router = DefaultRouter()

urlpatterns = [
                  path('', SupplierListAPIView.as_view(), name='suppliers_list'),
                  path('create/', SupplierCreateAPIView.as_view(), name='supplier_create'),
                  path('<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier_retrieve'),
                  path('<int:pk>/update/', SupplierUpdateAPIView.as_view(), name='supplier_update'),
                  path('<int:pk>/delete/', SupplierDestroyAPIView.as_view(), name='supplier_delete'),
                  path('contacts/', ContactListAPIView.as_view(), name='contacts_list'),
                  path('contacts/create/', ContactCreateAPIView.as_view(), name='contact_create'),
                  path('contacts/<int:pk>/', ContactRetrieveAPIView.as_view(), name='contact_retrieve'),
                  path('contacts/<int:pk>/update/', ContactUpdateAPIView.as_view(), name='contact_update'),
                  path('contacts/<int:pk>/delete/', ContactDestroyAPIView.as_view(), name='contact_delete'),
                  path('products/', ProductListAPIView.as_view(), name='products_list'),
                  path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
                  path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
                  path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
                  path('products/<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product_delete'),
              ] + router.urls
