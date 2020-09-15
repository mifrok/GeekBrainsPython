"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from random import random
class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        matrix = ''  # создает строку
        for i in self.matrix:
            for j in range(len(i)):
                i[j] = str(i[j])  # переводит значения в строку
            matrix = matrix + ' '.join(i) + '\n'  # добавляет значения в строку с пробелами, переводит на новую строку
        return matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other[i][j]

def create_matrix(len_gorzontal, len_vertical):
    matrix = []
    for i in range(len_vertical):
        matrix_element = [int(random()*10) for x in range(len_gorzontal)]
        matrix.append(matrix_element)
    return matrix


my_matrix = Matrix(create_matrix(3, 3))
print(my_matrix.matrix)
new_matrix = create_matrix(3, 3)
print(new_matrix)
my_matrix + new_matrix
print(my_matrix.matrix)
print(my_matrix)