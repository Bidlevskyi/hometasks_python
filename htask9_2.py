'''
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо
или влево, в зависимости от третьего параметра функции. Функция должна
 принимать три параметра: в первом параметре передаётся число для сдвига,
 второй параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на
 1 разряд), 3-й булевский параметр задаёт направление сдвига (по умолчанию
 влево (False)).
'''
'''
example
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
 
 
nums = [4, 5, 6, 7, 8, 9, 0]

'''
def sdig(n, r = 1, m = False):
    lst = list(map(int, str(n)))
    if m is False:
        for i in range(r):
            lst.append(lst.pop(i))
        nn = str(''.join(str(x) for x in lst))
        return(nn)

n = int(input('n = '))
r = int(input('r =' ))
print(sdig(n, r))




