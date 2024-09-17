'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b, c):
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        min = c
    s = a + b + c - min
    return s


print(my_func(1, 2, 3))


