
x = input("Your date: ")


def sum_1(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

c = True
while c:
    x = str(sum_1(x))
    if int(x) < 10:
        c = False

print(x)