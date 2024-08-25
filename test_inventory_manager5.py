import inventory_manager

```python
import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    
    def setUp(self):
        """Set up a basic inventory manager for testing."""
        self.manager = InventoryManager()

    def test_add_item_new(self):
        """Test adding a new item to the inventory."""
        result = self.manager.add_item("apple", 5)
        self.assertEqual(result, "Added 5 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 5)

    def test_add_item_existing(self):
        """Test adding to an existing item in the inventory."""
        self.manager.add_item("apple", 5)
        result = self.manager.add_item("apple", 3)
        self.assertEqual(result, "Added 3 apple(s) to inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 8)

    def test_remove_item_successful(self):
        """Test successfully removing items from the inventory."""
        self.manager.add_item("apple", 5)
        result = self.manager.remove_item("apple", 3)
        self.assertEqual(result, "Removed 3 apple(s) from inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 2)

    def test_remove_item_insufficient_quantity(self):
        """Test removing more items than are present in the inventory."""
        self.manager.add_item("apple", 2)
        result = self.manager.remove_item("apple", 5)
        self.assertEqual(result, "Error: Not enough apple in inventory.")
        self.assertEqual(self.manager.get_quantity("apple"), 2)

    def test_remove_item_not_found(self):
        """Test attempting to remove an item that is not in the inventory."""
        result = self.manager.remove_item("banana", 1)
        self.assertEqual(result, "Error: banana not found in inventory.")
        self.assertEqual(self.manager.get_quantity("banana"), 0)

    def test_get_quantity_existing_item(self):
        """Test getting the quantity of an existing item."""
        self.manager.add_item("apple", 5)
        self.assertEqual(self.manager.get_quantity("apple"), 5)

    def test_get_quantity_non_existing_item(self):
        """Test getting the quantity of a non-existing item."""
        self.assertEqual(self.manager.get_quantity("banana"), 0)

    def test_list_inventory(self):
        """Test listing the inventory."""
        self.manager.add_item("apple", 5)
        self.manager.add_item("banana", 3)
        expected_inventory = {"apple": 5, "banana": 3}
        self.assertEqual(self.manager.list_inventory(), expected_inventory)

if __name__ == "__main__":
    unittest.main()
```

### Explanation

1. **Imports**: We import `unittest` for the testing framework, and `InventoryManager` from the provided file.

2. **Setup Method**: The `setUp` method creates a new instance of `InventoryManager` before each test.

3. **Test Methods**:
    - **`test_add_item_new`**: Verifies adding a new item works correctly.
    - **`test_add_item_existing`**: Tests adding quantity to an existing item.
    - **`test_remove_item_successful`**: Confirms that a successful item removal is reflected in the inventory.
    - **`test_remove_item_insufficient_quantity`**: Ensures that attempting to remove more items than are available fails properly.
    - **`test_remove_item_not_found`**: Validates that removing a non-existent item returns the correct error.
    - **`test_get_quantity_existing_item`**: Checks retrieval of the quantity of an existing item.
    - **`test_get_quantity_non_existing_item`**: Tests retrieval of a non-existing item quantity, expecting zero.
    - **`test_list_inventory`**: Confirms that listing the inventory reflects all additions accurately.

These tests cover typical use cases and edge cases for inventory management, ensuring the `InventoryManager` class behaves as expected under various conditions.