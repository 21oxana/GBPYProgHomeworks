# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1 = [1.1, 1.2, 3.1, 5, 10.01]

var_list = [i - int(i) for i in list_1]
difference = max(var_list) - min(var_list) 

print(difference) 