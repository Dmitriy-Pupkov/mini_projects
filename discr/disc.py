from math import *


def disc(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'Корней нет'
    elif d == 0:
        x = b * -1 / (2 * a)
        return x
    elif d > 0:
        x1 = (b * -1 + sqrt(d)) / (2 * a)
        x2 = (b * -1 - sqrt(d)) / (2 * a)
        return x1, x2


a = int(input('Введите переменную а\n'))
b = int(input('Введите переменную b\n'))
c = int(input('Введите переменную c\n'))

print(disc(a, b, c))
