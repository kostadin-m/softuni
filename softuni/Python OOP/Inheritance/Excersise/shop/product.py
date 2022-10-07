class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, q):
        if self.quantity - q >= 0:
            self.quantity -= q

    def increase(self, q):
        self.quantity += q

    def __repr__(self):
        return self.name

