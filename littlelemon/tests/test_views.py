# tests/test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(
            Title='Burger', Price=10, Inventory=100)
        self.menu2 = Menu.objects.create(
            Title='Pizza', Price=12, Inventory=150)
        self.menu3 = Menu.objects.create(
            Title='Salad', Price=8, Inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
