import os
from time import sleep
rows = 21
cols = 22
for i in range(rows):
    if i <= rows // 2:
        for j in range(cols):
            if (    i == 0
                    or j == i
                    or j == rows - i
                ):
                print('*', end='')
            else:
                print(' ', end='')
    print()
