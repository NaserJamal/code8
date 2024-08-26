import inventory_manager

```python
import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        self.assertEqual(self.manager.add_item("apple", 5), "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.add_item("banana", 3), "Added 3 banana(s) to inventory.")
        self.assertEqual(self.manager.inventory, {"apple": 5, "banana": 3})

    def test_remove_item(self):
        self.manager.inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.remove_item("apple", 2), "Removed 2 apple(s) from inventory.")
        self.assertEqual(self.manager.inventory, {"apple": 3, "banana": 3})
        self.assertEqual(self.manager.remove_item("apple", 4), "Removed 3 apple(s) from inventory.")
        self.assertEqual(self.manager.inventory, {"banana": 3})
        self.assertEqual(self.manager.remove_item("orange", 1), "Error: orange not found in inventory.")

    def test_get_quantity(self):
        self.manager.inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.get_quantity("apple"), 5)
        self.assertEqual(self.manager.get_quantity("banana"), 3)
        self.assertEqual(self.manager.get_quantity("orange"), 0)

    def test_list_inventory(self):
        self.manager.inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.list_inventory(), {"apple": 5, "banana": 3})

if __name__ == '__main__':
    unittest.main()
```