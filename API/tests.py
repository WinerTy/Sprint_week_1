from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from database.models import Perevals


class TestAPI(TestCase):
    def test_api(self):
        response = self.client.get(reverse('api-v1'))
        self.assertEqual(response.status_code, 200)
