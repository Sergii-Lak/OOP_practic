class Descriptor:

    #def __init__(self, val):
    #    self.val = val

    def __get__(self, obj, obj_type):
        return self.val

    def __set__(self, obj, value):
        print(value)
        self.val = value

class Clas:

    atte = Descriptor()


ex = Clas()
ex.atte = 222