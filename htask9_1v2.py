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
def sysis(n, k):
    from string import ascii_uppercase
    a1 = ascii_uppercase
    s = []
    n1 = n
    while n1 >= k:
        r = n1 % k
        n1 = n1 // k
        s.append(r)
    s.append(n1)
    s.reverse()
    if k > 10:
        for x in range(0, len(s)):
            if s[x] >= 10:
                p = s[x] - 10
                del s[x]
                s.insert(x, a1[p])
    res = str(''.join(str(x) for x in s))
    print(res)

n = int(input('Enter volume = '))
k = int(input('Enter system = '))
sysis(n, k)
