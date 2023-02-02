# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Введите координаты X и Y:")
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(f"Координата ({x}, {y}) находится в первой четверти.")
elif x < 0 and y > 0:
    print(f"Координата ({x}, {y}) находится во второй четверти.")
elif x < 0 and y < 0:
    print(f"Координата ({x}, {y}) находится в третьей четверти.")
elif x > 0 and y < 0:
    print(f"Координата ({x}, {y}) находится в четвертой четверти.")