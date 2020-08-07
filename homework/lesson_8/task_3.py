'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
 Класс-исключение должен контролировать типы данных элементов списка.'''

class NewList(Exception):
    def __init__(self, txt):
        self.txt = txt

A = []
while True:
    data = input('Введите данные: ')
    if data == 's':
        break
    else:
        A.append(data)

try:
    for i in range(len(A)):
        if A[i].isdigit() == False:
            raise NewList(f"Вы ввели не число - {A[i]}")
except NewList as err:
    print(err)
else:
    print("Все хорошо.")