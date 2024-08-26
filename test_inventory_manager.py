import inventory_manager

import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        result = self.manager.add_item("apple", 5)
        self.assertEqual(result, "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.inventory["apple"], 5)

        result = self.manager.add_item("apple", 3)
        self.assertEqual(result, "Added 3 apple(s) to inventory.")
        self.assertEqual(self.manager.inventory["apple"], 8)

    def test_remove_item(self):
        self.manager.add_item("banana", 5)
        result = self.manager.remove_item("banana", 3)
        self.assertEqual(result, "Removed 3 banana(s) from inventory.")
        self.assertEqual(self.manager.inventory["banana"], 2)

        result = self.manager.remove_item("banana", 2)
        self.assertEqual(result, "Removed 2 banana(s) from inventory.")
        self.assertNotIn("banana", self.manager.inventory)

        result = self.manager.remove_item("banana", 1)
        self.assertEqual(result, "Error: banana not found in inventory.")

        self.manager.add_item("apple", 2)
        result = self.manager.remove_item("apple", 3)
        self.assertEqual(result, "Error: Not enough apple in inventory.")

    def test_get_quantity(self):
        self.manager.add_item("orange", 4)
        self.assertEqual(self.manager.get_quantity("orange"), 4)
        self.assertEqual(self.manager.get_quantity("grape"), 0)

    def test_list_inventory(self):
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        expected_inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.list_inventory(), expected_inventory)

if __name__ == '__main__':
    unittest.main()