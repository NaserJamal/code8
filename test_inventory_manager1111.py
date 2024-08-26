import inventory_manager


import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        self.assertEqual(self.manager.add_item("apple", 5), "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.add_item("banana", 3), "Added 3 banana(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 5)
        self.assertEqual(self.manager.get_quantity("banana"), 3)

    def test_remove_item(self):
        self.manager.add_item("apple", 5)
        self.assertEqual(self.manager.remove_item("apple", 2), "Removed 2 apple(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 3)
        self.assertEqual(self.manager.remove_item("apple", 4), "Removed 3 apple(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 0)
        self.assertEqual(self.manager.remove_item("banana", 1), "Error: banana not found in inventory.")

    def test_get_quantity(self):
        self.assertEqual(self.manager.get_quantity("apple"), 0)
        self.manager.add_item("apple", 5)
        self.assertEqual(self.manager.get_quantity("apple"), 5)

    def test_list_inventory(self):
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        self.assertEqual(self.manager.list_inventory(), {"apple": 5, "banana": 3})

if __name__ == "__main__":
    unittest.main()