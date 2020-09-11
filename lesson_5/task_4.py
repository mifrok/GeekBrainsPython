"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""
# Через if решение простое, пробую решить с помощью словаря
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('task4.txt', 'r', encoding='utf-8') as task4:
    file_strings = task4.readlines()
    for i in range(len(file_strings)):
        temp = file_strings[i].split()  # Разбиваем строку на элементы
        temp[0] = my_dict[temp[0]]  # Заменяем на совпадающий элемент в словаре по ключу
        file_strings[i] = ' '.join(temp)  # формируем строку обратно
with open('task4_result.txt', 'w', encoding='utf-8') as task4:
    for i in file_strings:
        task4.write(f'{i}\n')  # Добавляем перенос строки для каждого элемента
