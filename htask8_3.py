'''
4. Написать функцию `season`, принимающую 1 аргумент — номер месяца (от 1 до
 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна,
  лето или осень).
'''
def season(m):

    if m in [1, 2, 12]:
        return('wintera')
        return('winter')
    elif m in [3, 4, 5]:
        return('sping')
    elif m in [6, 7, 8]:
        return('summer')
    elif m in [9, 10, 11]:
        return('autumn')
m = int(input('Enter mouth: '))
print(season(m))
