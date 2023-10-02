from math import sqrt
# with open("17 (12).txt") as f:
#     numbers = list(map(int, f.read().split()))
#
# even = []
# for x in numbers:
#     if x % 2 == 0:
#         even.append(x)
#
# avg = sum(even) // len(even)
#
# count = 0
# max_sum = 0
# for i in range(len(numbers)-1):
#     a = numbers[i]
#     b = numbers[i+1]
#     if (a % 3 == 0 or b % 3 == 0) and (a < avg or b < avg):
#         count += 1
#         max_sum = max(max_sum, a+b)
#
# print(count, max_sum)


# x = 0
# while True:
#     x1 = x
#     L = 0
#     M = 0
#     while x1 > 0:
#         L = L+1
#         if (x1 % 2) != 0:
#             M = M + x1 % 8
#         x1 = x1 // 8
#     if L == 3 and M == 6:
#         print(x)
#     x += 1


# with open("24 (7).txt") as f:
#     ls = f.read()
#
# count = 0
# max_count = 0
# for i in range(len(ls)-3):
#     a = ls[i]
#     b = ls[i+1]
#     c = ls[i+2]
#     d = ls[i+3]
#     if a == "X" and b == "Z" and c == "Z" and d == "Y":
#         count = 3
#     else:
#         count += 1
#         max_count = max(max_count, count)
# print(max_count)


def divisor(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0 and n % i == 0:
            count += 1
            if count > 5:
                return False
    print(count)
    if count == 5:
        return True
    return False


for x in range(45000000, 45212177):
    if divisor(x):
        print(x)


