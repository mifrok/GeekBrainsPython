"""Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, x, y):
        self.number = complex(x, y)

    def __add__(self, other):
        self.number += other

    def __mul__(self, other):
        self.number *= other


number_1 = ComplexNumber(2, 3)
number_2 = ComplexNumber(3, 4)

number_1 + number_2.number
number_1 * number_2.number
number_2 + number_1.number
number_2 * number_1.number
print(number_1.number, number_2.number)