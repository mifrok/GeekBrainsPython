"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class ZeroDivizionException(Exception):
    def __init__(self, message):
        self.message = message


dividend = int(input('Type dividend: '))
divider = int(input('Type divider: '))
if divider == 0: raise ZeroDivizionException('Zero division error!')
print(dividend / divider)
