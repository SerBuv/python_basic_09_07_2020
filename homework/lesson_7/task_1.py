'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.'''

class Matrix:
    def  __init__(self, *data):
        self.data = list(data)
    def __str__(self):
        return f'Сумма элементов матрицы {self.data}'
    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0]]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(*result)
        min_m = min((self.data, other.data))
        max_m = max((self.data, other.data))
        result = list(map(sum, zip(self.data, other.data)))
        result.extend(max_m[len(min_m):])
m1 = Matrix([1, 2, 3], [4, 5, 6])
m2 = Matrix([5, 1, 4], [3, 1, 7])
m3 = m1 + m2
print(m3)
