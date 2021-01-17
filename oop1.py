# Statics methods in class

class Now1():
    __numb1 = 0

    def __init__(self, x = 0, y = 0):
        Now1.__numb1 += 1
        self.__x = x
        self.__y = y

    @staticmethod
    def getVal():
        return Now1.__numb1


pt = Now1()
pt2 = Now1()

print(Now1.getVal())