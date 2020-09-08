"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random, math

random_list = [math.floor(random.random() * 10) for number in range(20)]
result = [random_list[number] for number in range(1, len(random_list)) if random_list[number] > random_list[number - 1]]
print(random_list, result)