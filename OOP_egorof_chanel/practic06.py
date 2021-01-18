# ООП 30 Множественное наследование в Python. Multiple inheritance in Python
# https://www.youtube.com/watch?v=_475mVLClM8&list=PLQAt0m1f9OHvyjJNjZK_unnLwMOXPTja8&index=31&ab_channel=egoroff_channel

class Person:

    def __init__(self, x):
        self.x = x
        self.y = 3

    def result(self):
        print(f"Person {self.x} + {self.y}")

class Human:
    def __init__(self, y):
        self.x = 10
        self.y = y

    def result(self):
        print(f"Human {self.x} + {self.y}")

class I_am(Human, Person ):

    def __init__(self):
        Person.__init__(self, 200)
        super().__init__(100)
        self.z = 30

    def result(self):
        print("Who i am: ")
        super().result()
        Person.result(self)

a = I_am()

a.result()