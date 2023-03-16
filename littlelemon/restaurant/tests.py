from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(id= 1,title="IceCream", price=8.00, inventory=100)
        IceCream = MenuItem.objects.get(title="IceCream")
        self.assertEqual(IceCream.price, 8.00)
