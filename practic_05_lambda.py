import  random

sequences = [10,2,8,7,5,4,3,11,0,1]

lam1 = lambda x: x*x # print(lam1(3))
lam2 = lambda x, y: (x * y -2)*x  # print(lam2(2,3))
lam3 = list(map(lambda x: x * 2, sequences))  # print(list(lam3))
lam4 = filter(lambda x: x > 4, sequences) # print(list(lam4))
lam5 = filter(lambda n: n % 2 == 1, sequences)  # print(list(lam5))



# Рекурсия
def ex_rec(x):
    if x == 0:
        return "Yes"
    print(x)
    x -= 1
    return ex_rec(x)

print(ex_rec(5))


class P:

    def __init__(self):
        self.u = 10


    @property
    def my(self):
        return self.u * 2

    @my.setter
    def my(self, w):
        self.u -= w

e = P()
print(e.my)
e.my = 100
print(e.my)