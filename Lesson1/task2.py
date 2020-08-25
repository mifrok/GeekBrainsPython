"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
'''Первый вариант'''
userTime = int(input('Введите количество секунд: '))
hours = 0
minutes = 0
seconds = 0
if userTime >= 360:
    hours = userTime // 360
    userTime -= hours * 360
if userTime >= 60:
    minutes = userTime // 60
    userTime -= minutes * 60
seconds = userTime
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
'''Второй вариант'''
userTime = int(input('Введите количество секунд: '))
hours = userTime // 360
userTime -= hours * 360
minutes = userTime // 60
userTime -= minutes * 60
seconds = userTime
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')