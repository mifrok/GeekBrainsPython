"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def personal_information(name, surname, birth_date, city, email, phone_number):
    print('Имя - {}, Фамилия - {}, Дата рождения - {}, город проживания - {}, email - {}, телефон - {}'
          .format(name, surname, birth_date, city, email, phone_number))


personal_information(
    name=input('Введите Ваше имя: '),
    surname=input('Введите Вашу фамилию: '),
    birth_date=input('Введите Вашу дату рождения: '),
    city=input('Введите Ваш город проживания: '),
    email=input('Введите Ваш email: '),
    phone_number=input('Введите Ваш номер телефона: ')
)
