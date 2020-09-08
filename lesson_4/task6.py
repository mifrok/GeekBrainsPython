"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle


def my_func_a():
    new_list = []
    for el in count(int(input('Введите стартовое число: '))):
        if el > 10:
            return new_list
        print(el)
        new_list.append(el)


def my_func_b(some_list):
    count_cycle = 1
    for el in cycle(some_list):
        if count_cycle > 10:
            break
        print(el)
        count_cycle += 1


my_func_b(my_func_a())
