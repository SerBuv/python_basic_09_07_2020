'''6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

from itertools import count
from itertools import cycle
import time
#count
for el in count(100):
    if el > 107:
        break
    else:
        print(el)
#cycle
с = 0
for i in cycle('123'):
    if с > 9:
        break
    time.sleep(0.5)
    print(i)
    с += 1