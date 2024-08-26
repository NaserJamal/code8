import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        self.assertEqual(self.manager.add_item("apple", 5), "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 5)
        self.assertEqual(self.manager.add_item("apple", 3), "Added 3 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 8)

    def test_remove_item(self):
        self.manager.add_item("banana", 5)
        self.assertEqual(self.manager.remove_item("banana", 2), "Removed 2 banana(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("banana"), 3)
        self.assertEqual(self.manager.remove_item("banana", 5), "Error: Not enough banana in inventory.")
        self.assertEqual(self.manager.remove_item("orange", 1), "Error: orange not found in inventory.")

    def test_get_quantity(self):
        self.assertEqual(self.manager.get_quantity("apple"), 0)
        self.manager.add_item("apple", 10)
        self.assertEqual(self.manager.get_quantity("apple"), 10)

    def test_list_inventory(self):
        self.manager.add_item("banana", 3)
        self.manager.add_item("apple", 5)
        self.assertEqual(self.manager.list_inventory(), {"banana": 3, "apple": 5})
        self.manager.remove_item("banana", 3)
        self.assertEqual(self.manager.list_inventory(), {"apple": 5})

if __name__ == '__main__':
    unittest.main()