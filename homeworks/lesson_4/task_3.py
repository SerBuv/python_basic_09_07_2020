'''3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.'''

from random import randint

print([i for i in range(randint(20, 240)) if i % 20 == 0 or i % 21 == 0])