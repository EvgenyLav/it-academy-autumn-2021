"""Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет,  вывести сообщение о неверных данных.
"""
a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третьей стороны: '))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if a + b > c and a + c > b and b + c > a:
    print('Площадь треугольника =', s)
else:
    print('Введены неверные данные')