# for i in range(1, 999999999):
#     x = i
#     L = 0
#     M = 0
#     while x > 0:
#         L = L + 1
#         if (x % 2) != 0:
#             M = M + x % 8
#         x = x // 8
#     if L == 3 and M == 6:
#         print(i)

for i in range(9999):
    x = i
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x = x // 6

    if a == 2 and b == 4:
        print(i)