# одинаковые аргументы во всех экземпляров класса

class Human:

    __shared_dict = {
        "heas": 1,
        "hand":2,
        "legth":2
    }

    def __init__(self):
        self.__dict__ = self.__shared_dict

    def get_1(self, x):
        return x


class fis1(Human):
    def __init__(self):
        self.r = 3
        super().__init__()

    def le(self, x):
        self.r = x
        return self.r

class fis2(Human):
    pass

a = fis1()
a.x = 2
b = fis2()
print(b.__dict__)
print(a.__dict__==b.__dict__)
a.le(20)
print(a.__dict__==b.__dict__)
b = fis2()
print(b.__dict__)