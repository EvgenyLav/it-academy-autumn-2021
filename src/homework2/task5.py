""" Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические  операторы и условные операторы. n - вводится
"""
n = int(input("Введите n: "))
f1 = 1
f2 = 1
for i in range(2, n):
    f1, f2 = f2, f1 + f2
print("n-e число Фибоначи =", f2)