'''
12. Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
(пробелы важны!). Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного
числа
'''
k = int(input('Please enter an integer number: '))
k0 = str(k - 1)
k1 = str(k + 1)
print('The next number for the number', k, 'is', k1,"")
print('The previous number hor the number', k, 'is', k0,'.')


