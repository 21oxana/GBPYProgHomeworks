# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
5

number1 = int(input('Введите число: '))
number = number1
suma = 0

while number != 0:
    lastnumber = number % 10
    suma = suma + lastnumber
    number = number // 10
print(f'Сумма цифр числа {number1}', 'равна', suma)