'''
10. В списке все элементы различны. Поменяйте местами минимальный и
 максимальный элемент этого списка. Создавать новый список недопустимо.
'''
a = [1, 33, 5, 7, 2, 5, 99, 36, 3]
x = min(a)
y = max(a)
print(a)
print(id(a))
xi = a.index(x)
yi = a.index(y)
del a[xi]
a.insert(xi, y)
del a[yi]
a.insert(yi, x)
print(a)
print(id(a))
