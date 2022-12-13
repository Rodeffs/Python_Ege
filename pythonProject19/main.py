# with open("24 (2).txt") as file:
#     data = list(file.read())
#
# count = 1
# max_count = 1
# for i in range(1, len(data)-1):
#     if (data[i] == "a" and (data[i - 1] == "d" or data[i + 1] == "d")) or (data[i] == "d" and (data[i - 1] == "a" or data[i + 1] == "a")):
#         if count > max_count:
#             max_count = count
#         count = 1
#     count += 1
#
# print(max_count)
#

from math import sqrt


def dev(n):
    dev_ls = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dev_ls.append(i)
    if len(dev_ls) >= 5:
        return dev_ls[0]*dev_ls[1]*dev_ls[2]*dev_ls[3]*dev_ls[4]
    return 0


numbers = []

for i in range(500000001, 9999999999999):
    if 0 < dev(i) < i:
        numbers.append(dev(i))
    if len(numbers) == 5:
        print(numbers)
        break
