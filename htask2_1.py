#!/urs/bin/python3
'''
9. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
Программа получает на вход числа `n` и `k` и должна вывести искомое
количество яблок (два числа).

'''
n = int(input("Enter quantity of children: "))
k = int(input("Enter quantity of apples: "))
r = k // n
o = k - (r * n)
print("apples hor child: ", r)
print("apples in basket", o)



