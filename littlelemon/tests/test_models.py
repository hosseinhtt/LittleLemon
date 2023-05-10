from unittest import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(f"{item.Title}: {item.Price}", "IceCream: 80")
