"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [2422000; 2422080], простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.
"""
from math import sqrt


def prime_check(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 0

for i in range(2422000, 2422081):
    if prime_check(i):
        count += 1
        print(count, i)
