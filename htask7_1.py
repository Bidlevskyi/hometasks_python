'''
1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
    - Примечание. Эту задачу на Питоне можно решить в одну строчку.
'''
from random import randint
a = [randint(1, 20) for _ in range(15)]
print(a)
print('В списке одинаковых чисел: ', len(a) - len(set(a)))