'''2. Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента.'''

from random import randint
i = 0
A = []
B = []
while len(A) < 10:
    A.append(randint(0, 100))
for i in range(len(A)-1):
    if A[i+1] > A[i]:
        B.append(A[i+1])
print(A)
print(B)