'''Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

with open('task_4.txt', 'r', encoding='UTF-8') as my_f:
    f = my_f.readline()
    a = f.replace('One', 'Один')
    with open('task_4_new.txt', 'w', encoding='UTF-8') as my_p:
        my_p.write(a)
    f = my_f.readline()
    a = f.replace('Two', 'Два')
    with open('task_4_new.txt', 'a', encoding='UTF-8') as my_p:
        my_p.write(a)
    f = my_f.readline()
    a = f.replace('Three', 'Три')
    with open('task_4_new.txt', 'a', encoding='UTF-8') as my_p:
        my_p.write(a)
    f = my_f.readline()
    a = f.replace('Four', 'Четыре')
    with open('task_4_new.txt', 'a', encoding='UTF-8') as my_p:
        my_p.write(a)
