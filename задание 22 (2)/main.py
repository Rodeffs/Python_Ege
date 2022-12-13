"""
Укажите наибольшее десятичное число, при вводе которого на экране сначала напечатается 3, а затем 6.
x = int(input())
 L = 0
 M = 0
while x > 0 :
    L = L+1
    if (x % 2) != 0:
        M = M + x % 8
    x = x // 8
print(L)
print(M)
"""

x = 0
while True:
    x2 = x
    L = 0
    M = 0
    while x2 > 0:
        L = L + 1
        if (x2 % 2) != 0:
            M = M + x2 % 8
        x2 = x2 // 8
    if L == 3 and M == 6:
        print(x)
    x += 1
