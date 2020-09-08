"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('task5.txt', 'w+', encoding='utf-8') as task5:
    for i in range(10):
        task5.write(f'{str(round(random.random() * 10))} ')
    task5.seek(0)  # переходим в начало файла
    print(sum(map(int, task5.readline().split())))  # Читаем строку readline, разбиваем её split, интуем содержимое map,
    # считаем сумму sum
