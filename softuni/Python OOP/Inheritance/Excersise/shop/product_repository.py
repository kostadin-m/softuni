class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        if product not in self.products:
            self.products.append(product)

    def find(self, product):
        for x in self.products:
            if x.name == product:
                return x

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{x.name}: {x.quantity}" for x in self.products])
