"""Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
   общую цену в рублях и копейках за L товаров.
"""

M = int(input('Введите число рублей: '))
N = int(input('Введите число копеек: '))
S = int(input('Введите количество товара: '))
L = S * (100 * M + N)  # подсчет общей суммы
print(L // 100, "руб.", L % 100, "коп.")