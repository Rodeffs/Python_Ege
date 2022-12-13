# 7. Задание 25 № 27856
"""
def check(n):
    numbers = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            numbers.append(i)
    if len(numbers) == 6:
        return numbers
    return 0
for i in range(95632, 95651):
    if check(i):
        print(*check(i))

"""

# 8. Задание 25 № 27850
from math import sqrt


def check(n):
    max_del = 0
    count_del = 0
    sq = sqrt(n)
    if sq == int(sq):
        max_del = 1
        for i in range(2,  int(sq)):
            if n % i == 0:
                count_del += 2
                if max_del == 1:
                    max_del = n // i
        if count_del == 2:
            return max_del
        return 0
    return 0


for j in range(123456789, 223456790):
    c = check(j)
    if c:
        print(j, c)
