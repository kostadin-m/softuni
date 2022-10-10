class Account:
    def __init__(self,id,balance,pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if self.__pin != pin:
            return 'Wrong pin'
        return self.__id

    def change_pin(self,old,new):
        if old != self.__pin:
            return 'Wrong pin'
        self.__pin = new
        return 'Pin changed'