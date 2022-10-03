class Cup:

    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mil):
        if self.status() > mil:
            self.quantity += mil

    def status(self):
        return self.size - self.quantity
