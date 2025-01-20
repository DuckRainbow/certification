from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from retailing.models import (Contact, Product, Supplier)
from users.models import User


class ContactTestCase(APITestCase):
    """Класс для проверки корректности работы CRUD контактов"""

    def setUp(self):
        self.user = User.objects.create(email='test@example.ru', first_name='test_name', last_name='test_last_name')
        self.user.set_password('test')
        self.user.is_active = True
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.contact = Contact.objects.create(
            email='test@emai.ru',
            country='test_country',
            city='test_city',
            street='test_street',
            building='test_building'
        )

    def test_create_contact(self):
        """Создание контакта"""
        url = reverse('retailing:contact_create')
        data = {
            'email': 'test2@emai.ru',
            'country': 'test_country2',
            'city': 'test_city2',
            'street': 'test_street2',
            'building': 'test_building2'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertTrue(Contact.objects.all().exists())

    def test_contacts_list(self):
        """Вывод списка контактов"""
        url = reverse('retailing:contacts_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.contact.pk,
                    'email': self.contact.email,
                    'country': self.contact.country,
                    'city': self.contact.city,
                    'street': self.contact.street,
                    'building': self.contact.building,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_contact_retrieve(self):
        """Проверка корректности данных"""
        url = reverse('retailing:contact_retrieve', args=(self.contact.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['email'], self.contact.email)
        self.assertEqual(data['country'], self.contact.country)
        self.assertEqual(data['city'], self.contact.city)
        self.assertEqual(data['street'], self.contact.street)
        self.assertEqual(data['building'], self.contact.building)

    def test_contact_update(self):
        """Проверка обновления контактов"""
        url = reverse('retailing:contact_update', args=(self.contact.pk,))
        data = {
            'street': 'Тестовая улица',
            'building': 'Тестовое строение',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['street'], 'Тестовая улица')
        self.assertEqual(data['building'], 'Тестовое строение')

    def test_contact_delete(self):
        """Проверка удаления контакта"""
        url = reverse('retailing:contact_delete', args=(self.contact.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 0)


class ProductTestCase(APITestCase):
    """Класс для проверки корректности работы CRUD продуктов"""

    def setUp(self):
        self.user = User.objects.create(email='test@example.ru', first_name='test_name', last_name='test_last_name')
        self.user.set_password('test')
        self.user.is_active = True
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(
            title='test_title',
            type='test_type',
        )

    def test_create_product(self):
        """Создание продукта"""
        url = reverse('retailing:product_create')
        data = {
            'title': 'test_title2',
            'type': 'test_type2',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertTrue(Product.objects.all().exists())

    def test_products_list(self):
        """Вывод списка продуктов"""
        url = reverse('retailing:products_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.product.pk,
                    'title': self.product.title,
                    'type': self.product.type,
                    'date_of_release': self.product.date_of_release.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_product_retrieve(self):
        """Проверка корректности данных"""
        url = reverse('retailing:product_retrieve', args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], self.product.title)
        self.assertEqual(data['type'], self.product.type)

    def test_product_update(self):
        """Проверка обновления продуктов"""
        url = reverse('retailing:product_update', args=(self.product.pk,))
        data = {
            'title': 'title updated',
            'type': 'type updated',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['title'], 'title updated')
        self.assertEqual(data['type'], 'type updated')

    def test_product_delete(self):
        """Проверка удаления продукта"""
        url = reverse('retailing:product_delete', args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
