"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
months = ['январь',
          'февраль',
          'март',
          'апрель',
          'май',
          'июнь',
          'июль',
          'август',
          'сентябрь',
          'октябрь',
          'ноябрь',
          'декабрь']
seasons = ['зима',
           'весна',
           'лето',
           'осень']
user_input = int(input('Введите номер месяца (от 1 до 12): '))
if user_input < 3 or user_input == 12:  # Определить сезон
    season = seasons[0]
elif 2 < user_input < 6:
    season = seasons[1]
elif 5 < user_input < 9:
    season = seasons[2]
else:
    season = seasons[3]
print(f'{months[user_input - 1]}, {season}')


months = {1: 'январь',
          2: 'февраль',
          3: 'март',
          4: 'апрель',
          5: 'май',
          6: 'июнь',
          7: 'июль',
          8: 'август',
          9: 'сентябрь',
          10: 'октябрь',
          11: 'ноябрь',
          12: 'декабрь'}

seasons = {
    'зима': [1, 2, 12],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}
user_input = int(input('Введите номер месяца (от 1 до 12): '))
print(months[user_input])
if user_input in seasons['зима']:
    print('зима')
elif user_input in seasons['весна']:
    print('весна')
elif user_input in seasons['лето']:
    print('лето')
else:
    print('осень')
