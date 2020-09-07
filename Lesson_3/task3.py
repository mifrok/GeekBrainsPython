"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(a, b, c):
    if a >= b >= c or b >= a >= c:
        return a + b
    elif b >= c >= a or c >= b >= a:
        return b + c
    else:
        return a + c


print(my_func(0, 0, 0))
