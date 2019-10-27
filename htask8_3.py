'''
4. Написать функцию `season`, принимающую 1 аргумент — номер месяца (от 1 до
 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна,
  лето или осень).
'''
def season(m):
    if m in [1, 2, 12]:
        print('winter')
    elif m in [3, 4, 5]:
        print('sping')
    elif m in [6, 7, 8]:
        print('summer')
    elif m in [9, 10, 11]:
        print('autumn')
m = int(input('Enter mouth: '))
season(m)