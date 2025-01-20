from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestRegisterUser(APITestCase):
    """Проверка регистрации пользователя"""

    def test_successful_user_registration(self):
        url = reverse('users:register')
        data = {
            "first_name": "test_name",
            "last_name": "test_last_name",
            "email": "test@example.ru",
            "password": "test123456",
        }
        response = self.client.post(url, data, format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['email'], 'test@example.ru')
        self.assertEqual(data['first_name'], 'test_name')
        self.assertEqual(data['last_name'], 'test_last_name')
