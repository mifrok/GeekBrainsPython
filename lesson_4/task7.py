"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def my_factorial(n):
    """Факториал с помощью рекурсии (для тренировки)"""
    if n == 0:
        return 1
    else:
        return my_factorial(n - 1) * n


def my_factorial2(n):
    """Факультативно, реализация без рекурсии"""
    new_list = [1] + [0] * n
    for i in range(1, n + 1):
        new_list[i] = new_list[i - 1] * i
    return new_list[n]


def my_generator(n):
    for i in range(1, n):
        yield my_factorial(i)


for el in my_generator(5):
    print(el)


def test_my_func():
    """Факультативно, тест функций"""
    print('Test - OK' if my_factorial(6) == 720 else 'Test - FAILED')
    print('Test - OK' if my_factorial2(6) == 720 else 'Test - FAILED')


test_my_func()
