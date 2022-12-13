# def check(n):
#     for i in range(1, n):
#         if n % i == 0 and i % 10 == 8 and i != 8:
#             return i
#     return 0
#
#
# amount = 0
# x = 500001
# while amount < 5:
#     delit = check(x)
#     if delit:
#         print(x, delit)
#         x += 1
#         amount += 1
#     else:
#         x += 1

# with open("17 (6).txt") as f:
#     data = list(map(int, f.read().split()))
#
# count = 0
# max_sum = 0
# for i in range(10001):
#     for j in range(i+1, 10000):
#         summa = data[i] + data[j]
#         if summa % 7 == 0:
#             count += 1
#             if summa > max_sum:
#                 max_sum = summa
# print(count, max_sum)

# with open("24 (5).txt") as f:
#     data = f.read()
#
# letters = []
# for i in range(len(data)):
#     if data[i] == "E":
#         letters.append(data[i+1])
#
# count = 0
# max_count = 0
# letter = ""
# sort_letters = sorted(letters)
# for i in range(1, len(sort_letters)):
#     if sort_letters[i] == sort_letters[i-1]:
#         count += 1
#         if count > max_count:
#             max_count = count
#             letter = data[i]
#     else:
#          count = 0
#
# print(letter, max_count)

# x1 = 0
# while True:
#     x = x1
#     a = 0
#     b = 0
#     while x > 0:
#         c = x % 10
#         a += c
#         if c > b:
#             b = c
#         x //= 10
#     if a == 9 and b == 7:
#         print(x1)
#         break
#     x1 += 1


