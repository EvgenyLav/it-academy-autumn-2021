""" Найти самое длинное слово  в введенном  предложении.
    Учтите что в предложении есть знаки препинания.
"""
str_ = (input("Введите предложение: "))
punktuation = [
    ',', '.', ':', ';', '- ', '!', '?', '(', ')', '[', ']', '{',
    '}', "'", '"', '$', '%', '^', '*', '&', '#', '№', '`', '~', '+',
    '/', '@', '_', '=', '>', '<'
]
for mark in punktuation:
    str_ = str_.replace(mark, "")
words = str_.split()
print("Самое длинное слов: ", max(words, key=len))
