'''5. Реализовать формирование списка, используя функцию range() и возможности генератора.
 В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.'''

from random import randint
from functools import reduce

A = []
B = []
for i in range(10):
    A.append(randint(100, 1000))
    if A[i] % 2 == 0:
        B.append(A[i])
print(A)
print(B)

# with reduce
def my_func_1(prev_el, el):
    return prev_el * el

# without reduce
def my_func_2(B):
    comp = 1
    for i in B:
        comp = comp * i
    return comp

print(reduce(my_func_1, B))
print(my_func_2(B))