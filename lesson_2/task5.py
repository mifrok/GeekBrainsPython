"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''Первый способ'''
# my_list.sort(reverse=True)
# print(my_list)
# user_input = int(input('Введите число: '))
# my_list.append(user_input)
# my_list.sort(reverse=True)
# print(my_list)
'''Второй способ'''
# my_list.sort(reverse=True)
# print(my_list)
# user_input = int(input('Введите число: '))
# for num in my_list:
#     if num == user_input:
#         my_list.insert(my_list.index(num) + 1, user_input)
#         break
#     elif max(my_list) > user_input > min(my_list):
#         for number in range(len(my_list)):
#             if my_list[number] > user_input > my_list[number + 1]:
#                 my_list.insert(number + 1, user_input)
#                 break
#     elif user_input >= max(my_list):
#         my_list.insert(0, user_input)
#         break
#     else:
#         my_list.append(user_input)
#         break
# print(my_list)
