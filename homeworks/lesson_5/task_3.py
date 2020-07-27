'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
 их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''
A = []
staff_dict = {}
with open('task_3.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        key, value = line.split()
        staff_dict[key] = int(value)
    print(staff_dict)
    for key in staff_dict:
        if staff_dict[key] < 20000:
            A.append(key)
    print('Следующие сотрудники получают з/п менее 20000 руб.: ', A)

#print(staff_dict)
