"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('task2.txt', 'r', encoding='utf-8') as task2:
    task2_strings = task2.readlines()
    print(f'Количество строк в файле: {len(task2_strings)}')
    for i, k in enumerate(task2_strings):
        k.replace("\n", "")
        print(f'Количество букв в строке {i + 1}: {len(k)}')
        print(f'Количество слов в строке {i + 1}: {len(k.split())}')
