'''
5. Дан список чисел. Определите, сколько в этом списке элементов, которые
больше двух своих соседей, и выведите количество таких элементов. Крайние
элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
'''
from random import randint
m = int(input('Enter the number of list item: '))
a = [randint(1, 30) for _ in range(m)]
b = []
max = 0
print(a)
for i in range(1, m-2):
    if a[i-1] < a[i] > a[i+1]:
        max +=1
        b.append(a[i])
print('the number of items that are larger than their neighbors =', max)
print('volume of item', b)