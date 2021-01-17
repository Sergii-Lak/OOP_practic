# getter and setter with property

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print("get balance")
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):   # такое же название метода как и в гетере выше
        print("set balance")
        self.__balance = value

