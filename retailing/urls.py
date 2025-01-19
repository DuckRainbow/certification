from django.urls import path
from rest_framework.routers import DefaultRouter

from retailing.apps import RetailingConfig
from retailing.views import (
)

app_name = RetailingConfig.name

router = DefaultRouter()

urlpatterns = [
                  path('', .as_view(), name='_list'),
                  path('create/', .as_view(), name='_create'),
                  path('my_/', .as_view(), name='_mylist'),
                  path('<int:pk>/', .as_view(), name='_retrieve'),
                  path('<int:pk>/update/', .as_view(), name='_update'),
                  path('<int:pk>/delete/', .as_view(), name='_delete'),
              ] + router.urls
