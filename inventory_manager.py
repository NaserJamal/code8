class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        return f"Added {quantity} {item_name}(s) to inventory."

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                if self.inventory[item_name] == 0:
                    del self.inventory[item_name]
                return f"Removed {quantity} {item_name}(s) from inventory."
            else:
                return f"Error: Not enough {item_name} in inventory."
        else:
            return f"Error: {item_name} not found in inventory."

    def get_quantity(self, item_name):
        return self.inventory.get(item_name, 0)

    def list_inventory(self):
        return self.inventory

def main():
    manager = InventoryManager()
    print(manager.add_item("apple", 5))
    print(manager.add_item("banana", 3))
    print(manager.remove_item("apple", 2))
    print(manager.get_quantity("apple"))
    print(manager.list_inventory())

if __name__ == "__main__":
    main()