from django.test import TestCase
from restaurant.models import Menu
from django.forms.models import model_to_dict


# Define a custom function that converts Decimal to float
def model_to_dict_but_decimal_to_float (item):
    # Convert the item to a dictionary using model_to_dict
    item_dict = model_to_dict (item, fields = ['title', 'price', 'inventory'])
    # Convert the price field to a float using the float function
    item_dict ['price'] = float (item_dict ['price'])
    # Return the modified dictionary
    return item_dict


class MenuViewTest(TestCase):
    def setUp (self):
        self.item1 = Menu.objects.create (title="IceCream", price=80.88, inventory=100)
        self.item2 = Menu.objects.create (title="FireCream", price=90.9, inventory=110)
        self.item3 = Menu.objects.create (title="EarthCream", price=70, inventory=600)

    def test_getall (self):
        items = Menu.objects.all()
        #serialized_items = [model_to_dict(item, fields = ['title', 'price', 'inventory']) for item in items]
        serialized_items = [model_to_dict_but_decimal_to_float (item) for item in items]
        #print(serialized_items[0])
        expected_response = [
            {"title": "IceCream", "price": 80.88, "inventory": 100},
            {"title": "FireCream", "price": 90.9, "inventory": 110},
            {"title": "EarthCream", "price": 70, "inventory": 600}
        ]
        self.assertEqual (serialized_items, expected_response)


