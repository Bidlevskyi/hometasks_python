'''
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.

  A         *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *




  B         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *



  C         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   *
    *               *
      *           *
        *       *
          *   *
            *


  D         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         *
    *       *       *
      *     *     *
        *   *   *
          * * *
            *
'''

rows = int(input("введите не четное количество строк: "))
cols = int(input("введите не четное количество столбцов: "))
# A
print('A')
for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (j == (cols // 2)-i or j ==(cols // 2)+i or i == rows // 2):
            print('*', end='')
        else:
            print(' ', end='')
    print()

# B
print('B')
for i in range(rows):
    print(i, end='\t')
    if i <= rows // 2:
        for j in range(cols):
            if (((cols // 2)-i) <= j <=  ((cols // 2)+i) or i == rows // 2):
                print('*', end='')
            else:
                print(' ', end='')
    print()

# C
print('C')
for i in range(rows):
    print(i, end='\t')
    if i <= rows // 2:
        for j in range(cols):
            if (((cols // 2)-i) <= j <=  ((cols // 2)+i) or i == rows // 2):
                print('*', end='')
            else:
                print(' ', end='')
    else:
        for j in range(cols):
            if (j == (i - (rows // 2))  or j == (cols -(1 + i - rows // 2))):
                print('*', end='')
            else:
                print(' ', end='')
    print()
# D
print('D')
for i in range(rows):
    print(i, end='\t')
    if i <= rows // 2:
        for j in range(cols):
            if (((cols // 2)-i) <= j <=  ((cols // 2)+i) or i == rows // 2):
                print('*', end='')
            else:
                print(' ', end='')
    else:
        for j in range(cols):
            if (j == (i - (rows // 2))  or j == (cols -(1 + i - rows // 2))
                or j == cols //2):
                print('*', end='')
            else:
                print(' ', end='')
    print()
