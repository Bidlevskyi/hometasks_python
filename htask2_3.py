'''
13. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то
же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть
не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из
трех классов.
'''
a = int(input('Enter quantity of students in class a: '))
b = int(input('Enter quantity of students in class b: '))
c = int(input('Enter quantity of students in class c: '))
d = (a + b + c) % 2
print('For all students need tables: ', ((a + b + c) // 2) + ((d) ** 0))
