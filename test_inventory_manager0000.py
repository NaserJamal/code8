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

    def test_remove_item_existing(self):
        self.manager.add_item("apple", 5)
        result = self.manager.remove_item("apple", 2)
        self.assertEqual(result, "Removed 2 apple(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 3)

    def test_remove_item_not_enough(self):
        self.manager.add_item("apple", 3)
        result = self.manager.remove_item("apple", 5)
        self.assertEqual(result, "Error: Not enough apple in inventory.")

    def test_remove_item_not_found(self):
        result = self.manager.remove_item("banana", 1)
        self.assertEqual(result, "Error: banana not found in inventory.")

    def test_remove_item_zero_quantity(self):
        self.manager.add_item("apple", 2)
        self.manager.remove_item("apple", 2)
        result = self.manager.remove_item("apple", 1)
        self.assertEqual(result, "Error: apple not found in inventory.")

    def test_get_quantity_existing(self):
        self.manager.add_item("apple", 5)
        self.assertEqual(self.manager.get_quantity("apple"), 5)

    def test_get_quantity_not_found(self):
        self.assertEqual(self.manager.get_quantity("banana"), 0)

    def test_list_inventory_empty(self):
        self.assertEqual(self.manager.list_inventory(), {})

    def test_list_inventory_non_empty(self):
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        self.assertEqual(self.manager.list_inventory(), {"apple": 5, "banana": 3})

if __name__ == "__main__":
    unittest.main()