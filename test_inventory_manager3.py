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
        
        # Test adding more of the same item
        result = self.manager.add_item("apple", 3)
        self.assertEqual(result, "Added 3 apple(s) to inventory.")
        self.assertEqual(self.manager.inventory["apple"], 8)

    def test_remove_item(self):
        self.manager.add_item("banana", 3)
        
        # Removing some of the items
        result = self.manager.remove_item("banana", 2)
        self.assertEqual(result, "Removed 2 banana(s) from inventory.")
        self.assertEqual(self.manager.inventory["banana"], 1)

        # Removing the remaining item
        result = self.manager.remove_item("banana", 1)
        self.assertEqual(result, "Removed 1 banana(s) from inventory.")
        self.assertNotIn("banana", self.manager.inventory)

        # Trying to remove more than exists
        result = self.manager.remove_item("banana", 1)
        self.assertEqual(result, "Error: banana not found in inventory.")

        # Trying to remove from an empty inventory
        result = self.manager.remove_item("orange", 1)
        self.assertEqual(result, "Error: orange not found in inventory.")

    def test_get_quantity(self):
        self.manager.add_item("apple", 10)
        quantity = self.manager.get_quantity("apple")
        self.assertEqual(quantity, 10)

        # Test getting quantity of an item not in inventory
        quantity = self.manager.get_quantity("banana")
        self.assertEqual(quantity, 0)

    def test_list_inventory(self):
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        inventory = self.manager.list_inventory()
        self.assertEqual(inventory, {"apple": 5, "banana": 3})
        
        # Test listing after removing all of an item
        self.manager.remove_item("banana", 3)
        inventory = self.manager.list_inventory()
        self.assertEqual(inventory, {"apple": 5})

if __name__ == '__main__':
    unittest.main()