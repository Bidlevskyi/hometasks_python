'''
9. Написать функцию для перевода десятичного числа в другую систему исчисления
(2-36).
Небольшая подсказка. В этой задаче вам понадобится:
	- список
	- метод revers() (или срез [::-1], или вместо revers() использовать
	  insert() тогда не придётся разворачивать список), чтоб развернуть список,
	 метод join()
	- строка ascii_uppercase из модуля string (её можно получить если сделать
	 импорт from string import ascii_uppercase), она содержит все буквы
	  латинского алфавита.
'''
def per(n):
    b = []
    n1 = n
    s = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4',
        '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9',
        '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E',
        '1111': 'F'
        }
    v = {
        '000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6,
        '111': 7
        }
    #двоичная система счисления
    while n1 > 0:
        if n1 % 2 == 0:
            b.insert(0, 0)
        else:
            b.insert(0, 1)
        n1 = n1 // 2
    lst = ''.join([str(x) for x in b])
    print('Число в двоичной системе', lst)
    #восмеричная система
    b2 = b.copy()
    b8 =[]
    if len(b2) % 4 != 0:
        while len(b2) % 3 !=0:
            b2.insert(0, 0)
    for a in range(2, len(b2), 3):
        z = str(''.join(str(x) for x in b2[a - 2:a + 1]))
        b8.append((v[str(z)]))
    lst8 = ''.join([str(x) for x in b8])
    print('число в восмеричной системе счисления', lst8)
    #шеснадцатиричная система счисления
    b1 = b.copy()
    b16 =[]
    if len(b1) % 4 != 0:
        while len(b1) % 4 !=0:
            b1.insert(0, 0)
    for a in range(3, len(b1), 4):
        o = str(''.join(str(x) for x in b1[a-3:a+1]))
        b16.append((s[str(o)]))
    lst16 = ''.join([str(x) for x in b16])
    print('число в шеснадцатиричной системе', lst16)
    print('Проверка\n',
          'Двоичная система счисления', bin(n), '\n'
          'Восмеричная система счисления', oct(n), '\n'
          'Шеснадсатиричная система счисления', hex(n)
          )

n = int(input('enter volume: '))
per(n)