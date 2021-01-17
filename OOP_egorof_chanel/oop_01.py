
class Decript:

    def __init__(self, x=2):
        self.__x = x

    def __get__(self, instance, owner):
        print(f"Its {self.__x}")
        return self.__x

    def __set__(self, instance, value):
        self.__x = value

class Person:

    x = Decript()

    @staticmethod
    def op():
        print("rrrr")


p = Person()
p.x = 44
p.x
