'''
2. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
 в первом списке, так и во втором.
    - Примечание. Эту задачу на Питоне можно решить в одну строчку.

'''
from random import randint
a = [randint(1, 10) for _ in range(10)]
b = [randint(1, 10) for _ in range(10)]
print(a)
print(b)
print('В двух списках одновременно содержиться чисел:',
      len((set(a)).intersection(set(b))))
