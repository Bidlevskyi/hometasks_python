'''
2. Написать функцию `is_year_leap`, принимающую 1 аргумент — год, и
 возвращающую True, если год високосный, и False
иначе.
'''
def is_year_leap(g):
    if (g % 4 == 0) and (g % 100 != 0):
        print('True')
    elif (g % 400 == 0):
        print('True')
    else:
        print('False')
g = int(input('Enter year: '))
is_year_leap(g)


