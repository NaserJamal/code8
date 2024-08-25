import inventory_manager

import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item_new(self):
        result = self.manager.add_item("apple", 5)
        self.assertEqual(result, "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 5)

    def test_add_item_existing(self):
        self.manager.add_item("apple", 5)
        result = self.manager.add_item("apple", 3)
        self.assertEqual(result, "Added 3 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 8)

    def test_remove_item_success(self):
        self.manager.add_item("banana", 5)
        result = self.manager.remove_item("banana", 3)
        self.assertEqual(result, "Removed 3 banana(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("banana"), 2)

    def test_remove_item_not_enough(self):
        self.manager.add_item("banana", 2)
        result = self.manager.remove_item("banana", 3)
        self.assertEqual(result, "Error: Not enough banana in inventory.")

    def test_remove_item_not_found(self):
        result = self.manager.remove_item("orange", 1)
        self.assertEqual(result, "Error: orange not found in inventory.")

    def test_get_quantity_existing(self):
        self.manager.add_item("apple", 5)
        quantity = self.manager.get_quantity("apple")
        self.assertEqual(quantity, 5)

    def test_get_quantity_non_existing(self):
        quantity = self.manager.get_quantity("banana")
        self.assertEqual(quantity, 0)

    def test_list_inventory(self):
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        expected_inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.list_inventory(), expected_inventory)

    def test_remove_all_items(self):
        self.manager.add_item("apple", 5)
        self.manager.remove_item("apple", 5)
        self.assertEqual(self.manager.get_quantity("apple"), 0)
        self.assertNotIn("apple", self.manager.inventory)

if __name__ == '__main__':
    unittest.main()