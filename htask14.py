from pprint import pprint as pp
from os import SEEK_SET
lst_0 = [
 'Андрей Говорухи\t\t 6 6 1 4 9 9 10 4 8 2 3 8\n',
 'Василий Петров\t\t 2 9 4 7 6 6 3 6 5 5 2 4\n',
 'Гавриил Варфаломеев\t 10 10 4 10 7 9 4 6 8 1 1 1\n',
 'Игнат Тюльпанов\t\t 8 1 4 1 1 5 2 5 2 2 10 8\n',
 'Илья Муромцев\t\t 1 6 4 7 10 9 5 3 7 4 7 2\n',
 'Кощей Бессмертный\t 3 10 1 4 1 8 10 6 2 10 7 4\n',
 'Максим Мухин\t\t 10 8 9 9 5 8 6 5 7 2 4 10\n',
 'Маргарита Мартынова\t 9 1 5 1 10 10 2 4 4 9 8 10\n',
 'Петр Николаев\t\t 2 9 5 9 1 2 8 7 8 1 9 1\n',
 'Полина Гусева\t\t 9 2 8 7 3 9 9 5 1 9 2 6\n',
 'Спиридов Тереньтьев\t 4 7 7 3 10 9 7 2 10 9 8 1\n',
 'Станислав Трердолобов\t 8 1 6 1 4 1 10 8 8 1 8 8\n'
]
file = open('file1.txt', 'w')
file.seek(0, 0)
for line in lst_0:
    file.write(line)
file.close()

file = open('file1.txt', 'r')
file.seek(0, 0)
lst = []
lst = file.readlines()
file.close()
########## bad code
lst1 = list(map(lambda x: x.strip('\n'), lst))
lst2 =(list(map(lambda x: x.replace('\t', ''), lst1)))
lst3 = list(map(lambda x: x.split(), lst2))
# print(lst3)
# print(sum(lst3[0][2:]))
s = list(map(lambda x: (x[0], '{}\t\t'.format(x[1])), lst3))
#sum(int(x[2:])/(len(x)-2)))
1
print(s)
