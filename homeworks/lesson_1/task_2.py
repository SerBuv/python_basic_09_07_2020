# 2. Пользователь вводит время в секундах. Переведите время
# в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_sec = int(input('Введите время в секундах: '))

time_hour = time_sec // 3600
more_sec = time_sec % 3600

time_min = more_sec // 60
time_sec = more_sec % 60

time = f'{time_hour}:{time_min}:{time_sec}'
print('Время в фотмате чч:мм:сс: ', time)