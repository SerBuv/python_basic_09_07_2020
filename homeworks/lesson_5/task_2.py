'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.'''

my_f = open("task_2.txt", "r", encoding='UTF-8')
lengh = my_f.readlines()
print('Количество строк - ', len(lengh))
count = 1
for i in lengh:
    a = i.split()
    print(f'Количество слов {count} строки:', len(a))
    count += 1
my_f.close()