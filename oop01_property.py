# Property objects, descryptors
# https://www.youtube.com/watch?v=zwel95I7O88&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=4&ab_channel=selfedu

class CordValue:

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:

    cordX = CordValue()
    cordY = CordValue()

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def w2(self):
        return "wwwww"

    @property                 # property - Декоратор, который позволяет методам выступать в роли атрибутов.
    def property_attr(self):
        return "I'm a read-only property!"

    #def __getCordX(self):
    #    print("chitaem znachenie iz __GetCordX")
    #    return self.__x
#
    #def __setCordX(self, x):
    #    print(f"zapisuvaem v __setCordX znachenie {x}")
    #    self.__x = x
#
    #cordX = property(__getCordX, __setCordX)

pt = Point(1, 2)
pt.cordX = 100   # zapisuvaem znachenie
print(pt.cordX)     # chitaem znachenie

s = pt.property_attr
s2 = pt.w2()
print(type(s))
print(s2)