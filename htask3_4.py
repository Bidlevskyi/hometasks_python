'''
5. Программа запрашивает ввод последовательности целых чисел, пока не будет
введён 0. Как только будет введён 0 (ноль), программа должна посчитать и
 вывести на экран:
- количество введённых чисел (завершающий 0 не считается)
- их сумму
- произведение
- среднее арифметическое (не считая завершающего числа 0)
- определить значение и порядковый номер наибольшего элемента последовательно-
сти. Если наибольших элементов несколько, выведите порядковый номер первого из
 них. Нумерация элементов начинается с 1 (еденицы)
- определить количество чётных и не чётных элементов в последовательности
- количество положительных и отрицательных значений
'''
counter = 1
imax = 0 # number of max volume
max = 0 # max volume
even = 0
odd = 0
s = 0  # sum
p = 1 # composition
positive = 0
negative = 0
while True:
    n = int(input("Enter volume: "))
    if n == 0:
        break
    if not n % 2:
        even += 1
    else:
        odd += 1
    if n > max:
        max = n
        imax = counter
    if n > 0:
        positive += 1
    else:
        negative += 1
    s = s + n
    p = p * n
    counter += 1
print('counter: ', counter)
print('sum: ', s)
print('composition: ', p)
print('average: ', s / counter)
print('maximum volume: ', max, 'number maximum volume: ', imax)
print('odd: ', odd)
print('even: ', even)
print('positive: ', positive)
print('negative: ', negative)
