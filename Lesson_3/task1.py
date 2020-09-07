"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_division(x, y):
    while True:
        try:
            return x / y
        except ZeroDivisionError:
            y = int(input('Деление на ноль недопустимо! Введите корректный делитель: '))
            continue


while True:
    try:
        x, y = int(input('Введите делимое число: ')), int(input('Введите делитель: '))
        break
    except ValueError:
        print('Введено некорректное число!')
        continue
print(my_division(x, y))