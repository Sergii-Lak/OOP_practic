# Сумма двух чисел которые вводятся в одну строку через пробел

def sum_numbers():
    a,b = map(int, input().split())
    return a + b

print(sum_numbers())

print(sum(map(int, input().split())))