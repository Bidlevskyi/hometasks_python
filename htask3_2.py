'''
Дано натуральное число. Требуется определить, является ли год с данным номером
високосным. Если год является високосным, то выведите `YES`, иначе выведите
 `NO`. Напомним, что в соответствии с григорианским календарем, год
является високосным, если его номер кратен 4, но не кратен 100, а также если
 он кратен 400.
'''
g = int(input("enter year: "))
if g <= 0:
    print('invalid volume')
    exit(0)
if (g % 4 == 0) and (g % 100 != 0):
    print('yes')
elif (g % 400 == 0):
    print('yes')
else:
    print('no')
