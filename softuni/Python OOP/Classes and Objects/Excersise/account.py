class Account:
    def __init__(self,id,name,balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self,balance):
        self.balance += balance
        return self.balance

    def debit(self,balance):
        if balance <= self.balance:
            self.balance -= balance
            return self.balance
        return f'Amount exceeded balance'

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'

