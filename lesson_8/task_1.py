"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    @classmethod
    def data_to_number(cls, date):
        return ''.join(date.split('-'))

    @staticmethod
    def check_is_data_correct(date):
        return 'Date is correct' if 1 <= int(date.split('-')[1]) <= 12 else \
            'Incorrect Date'


date = '11-07-2020'
date1 = '12-21-2222'

print(Date.data_to_number(date))
print(Date.data_to_number(date1))
print(Date.check_is_data_correct(date))
print(Date.check_is_data_correct(date1))
