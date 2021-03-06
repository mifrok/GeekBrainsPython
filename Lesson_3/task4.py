"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func1(x, y):
    """Возведение в отрицательную степень стандартным методом Python x ** y"""
    return x ** y


def my_func2(x, y):
    """Возведение в отрицательную степень рекурсивным алгоритмом"""
    y = abs(y)
    if y == 0:
        return 1
    else:
        return my_func2(x, y - 1) / x


def my_func3(x, y):
    """Возведение в отрицательную степерь циклом"""
    result = 1
    y = abs(y)
    for i in range(y):
        result *= x
    return 1 / result


def test_my_func():
    """Тестирование на корректность работы функций"""
    for x in range(1, 10):
        for y in range(-5, -1, 1):
            answer = round(x ** y, 10) # Использовал округление, так как тесты ругались при расхождениях на 18-19 знаках
            test1 = round(my_func1(x, y), 10)
            print('test1 - OK' if test1 == answer else 'test1 - FAIL')
            test2 = round(my_func2(x, y), 10)
            print('test2 - OK' if test2 == answer else 'test2 - FAIL')
            test3 = round(my_func3(x, y), 10)
            print('test3 - OK' if test3 == answer else 'test3 - FAIL')


test_my_func() # Тестирование

# Ввод значений пользователем, проверка на корректность введенных данных, печать результатов работы всех функций
while True:
    try:
        x = int(input('Введите целое положительное число: '))
        if x <= 0:
            print('Введено некорректное число!')
            continue
        y = int(input('Введите целое отрицательно число: '))
        if y >= 0:
            print('Введено некорректное число!')
            continue
        break
    except ValueError:
        print('Введено некорректное число!')
        continue
print(my_func1(x, y), my_func2(x, y), my_func3(x, y), sep='\n')
