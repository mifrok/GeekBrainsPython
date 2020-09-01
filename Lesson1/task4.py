"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
userNumber = int(input('Введите целое положительное число: '))
maxNumber = 0
while userNumber >= 1:
    newMaxNumber = userNumber % 10
    if newMaxNumber > maxNumber:
        maxNumber = newMaxNumber
    userNumber = (userNumber - newMaxNumber) / 10
print(int(maxNumber))