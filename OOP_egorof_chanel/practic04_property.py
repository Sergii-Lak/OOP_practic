
class Square:

    def __init__(self, s):
        self.__s = s
        self.__n = None   # значение для кеша который хранит уже вычисленный квадрат числа

    @property
    def get_val(self):
        return self.__s

    @get_val.setter
    def get_val(self, value):  # сеттер когда мы вводим или меняем значение сбрасывает кеш на None
        self.__s = value
        self.__n = None

    @property
    def calculate_square(self):
        if self.__n is None:
            print("Calculate square!")  # выводится первый раз когда вычисляется значение
            self.__n = self.__s ** 2
        return self.__s ** 2


t1 = Square(3)


print(t1.calculate_square)
print(t1.calculate_square)