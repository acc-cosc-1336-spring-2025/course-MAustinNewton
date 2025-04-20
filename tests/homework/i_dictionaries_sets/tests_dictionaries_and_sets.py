import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget, inventory_dictionary

class Test_Config(unittest.TestCase):

    def setUp(self):
        # Reset the inventory for each test
        inventory_dictionary.clear()

    def test_add_inventory(self):
        add_inventory("Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        add_inventory("Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        add_inventory("Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        add_inventory("Widget1", 20)
        add_inventory("Widget2", 30)

        result = remove_inventory_widget("Widget1")
        self.assertEqual(result, "Record deleted")
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertIn("Widget2", inventory_dictionary)

        result = remove_inventory_widget("Widget3")
        self.assertEqual(result, "Item not found")
