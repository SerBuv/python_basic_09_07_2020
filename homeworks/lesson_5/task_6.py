'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
 и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
 чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.'''

staff_sum = {}
staff_dict = {}
with open('task_6.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        key, *value = line.split()
        staff_dict[key] = (value)
    print(staff_dict)
    for key in staff_dict:
        res = list(map(lambda sub: int(''.join([ele for ele in sub if ele.isnumeric()])), staff_dict[key]))
        staff_sum[key] = (sum(res))
    print(staff_sum)
