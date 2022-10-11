class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item):
        if sum(self.items.values()) == self.capacity:
            return f"Not enough capacity in the shop"
        self.items[item] = self.items.get(item, 0) + 1
        return f"{item} added to the shop"

    def remove_item(self, item, amount):
        if item not in self.items or amount > self.items[item]:
            return f"Cannot remove {amount} {item}"
        self.items[item] -= amount
        if not self.items[item]:
            del self.items[item]
        return f"{amount} {item} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
