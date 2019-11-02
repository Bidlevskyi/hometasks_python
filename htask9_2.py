'''
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо
или влево, в зависимости от третьего параметра функции. Функция должна
 принимать три параметра: в первом параметре передаётся число для сдвига,
 второй параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на
 1 разряд), 3-й булевский параметр задаёт направление сдвига (по умолчанию
 влево (False)).
'''

def sdig(n, r = 1, m = False):
    lst = list(map(int, str(n)))
    if m == False:
        for i in range(r):
            lst.append(lst.pop(0))
    else:
        for i in range(r):
            lst.insert(0, lst.pop(-1))
    nn = str(''.join(str(x) for x in lst))
    return(nn)

n = int(input('Введите число: '))
r = int(input('Введите количество разрядов для сдвига ' ))
m = bool(input('Введите направление сдвига(0 - влево, 1 - вправо)'))
print(sdig(n, r, m))




