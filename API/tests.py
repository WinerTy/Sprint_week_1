import json


from django.test import TestCase
from django.urls import reverse
from icecream import ic

from database.models import Perevals

'''
Тестирование API

'''


# Класс TestAPI предназначен для тестирования страниц с документацией
class TestAPI(TestCase):
    def test_page_docs(self):
        response = self.client.get(reverse('schema-swagger-ui'))
        self.assertEqual(response.status_code, 200)

    def test_page_redoc(self):
        response = self.client.get(reverse('schema-redoc'))
        self.assertEqual(response.status_code, 200)


# Класс APIMethodTestCase предназначен для тестирования методов API
class APIMethodTestCase(TestCase):

    def test_get_request(self):
        ic('Тестрование GET метода')
        url = reverse('submitdata-list')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        ic('Конец теста GET метода')

    def test_post_request(self):
        ic('Начало теста POST метод')
        url = reverse('submitdata-list')
        data = {
            "beauty_title": "TestAPIPOST",
            "title": "TestAPIPOST",
            "other_titles": "TestAPIPOST",
            "connect": "TestAPIPOST",
            "status": "new",
            "add_time": "2024-01-27 15:23:35",
            "level": {
                "summer": "2B",
                "autumn": "2A",
                "winter": "1A",
                "spring": "3C"
            },
            "user": {
                "fam": "TestAPIPOST",
                "name": "TestAPIPOST",
                "otc": "TestAPIPOST",
                "email": "exampleasdTestAPIPOST2@emaple.com",
                "phone": 123456789
            },
            "coord": {
                "latitude": 222.0,
                "longitude": 221232.0,
                "height": 222
            },
            "images": [
                {
                    "title": "test",
                    "image": "https://img.freepik.com/free-photo/a-cupcake-with-a-strawberry-on-top-and-a-strawberry-on-the-top_1340-35087.jpg"
                }
            ]
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)  # Ожидаем, что статус ответа будет 201 (Created)
        new_object = Perevals.objects.last()
        ic(new_object)
        ic('Конец POST метода')

    def test_patch_request(self):
        ic('Начало теста PATCH метод')
        url = reverse('submitdata-list')
        data = {
            "beauty_title": "TestAPIPOST",
            "title": "TestAPIPOST",
            "other_titles": "TestAPIPOST",
            "connect": "TestAPIPOST",
            "status": "new",
            "add_time": "2024-01-27 15:23:35",
            "level": {
                "summer": "2B",
                "autumn": "2A",
                "winter": "1A",
                "spring": "3C"
            },
            "user": {
                "fam": "TestAPIPOST",
                "name": "TestAPIPOST",
                "otc": "TestAPIPOST",
                "email": "exampleasdTestAPIPOST2@emaple.com",
                "phone": 123456789
            },
            "coord": {
                "latitude": 222.0,
                "longitude": 221232.0,
                "height": 222
            },
            "images": [
                {
                    "title": "test",
                    "image": "https://img.freepik.com/free-photo/a-cupcake-with-a-strawberry-on-top-and-a-strawberry-on-the-top_1340-35087.jpg"
                }
            ]
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Получаем ID созданного объекта
        new_object_id = response.json()['id']
        ic(new_object_id, 'Был получен ID созданного объекта при тесте PATCH')

        # Теперь выполняем запрос PATCH
        patch_url = reverse('submitdata-detail', kwargs={'pk': new_object_id})
        patch_data = {
            "beauty_title": "TestAPIPatch",
            "title": "TestAPIPOST",
            "other_titles": "TestAPIPOST",
            "connect": "TestAPIPOST",
            "status": "new",
            "add_time": "2024-01-27 15:23:35",
            "level": {
                "summer": "2B",
                "autumn": "2A",
                "winter": "1A",
                "spring": "3C"
            },
            "user": {
                "fam": "TestAPIPOST",
                "name": "TestAPIPOST",
                "otc": "TestAPIPOST",
                "email": "exampleasdTestAPIPOST2@emaple.com",
                "phone": 123456789
            },
            "coord": {
                "latitude": 222.0,
                "longitude": 221232.0,
                "height": 222
            },
            "images": [
                {
                    "title": "test",
                    "image": "https://img.freepik.com/free-photo/a-cupcake-with-a-strawberry-on-top-and-a-strawberry-on-the-top_1340-35087.jpg"
                }
            ]
        }
        patch_response = self.client.patch(patch_url, json.dumps(patch_data), content_type='application/json')
        self.assertEqual(patch_response.status_code, 200)

        updated_object = Perevals.objects.get(id=new_object_id)
        ic(updated_object, 'Объект был обновлен')
        ic('Конец PATCH метода')
