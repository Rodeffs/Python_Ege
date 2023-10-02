"""
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
- символ «?» означает ровно одну произвольную цифру;
- символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.

Среди натуральных чисел, больших 4679000, найдите числа, все простые делители которых, выписанные без пробелов по возрастанию, образуют число, соответствующее маске «27*39?» или «34*2?7».

Например, число 234566 имеет 3 простых делителя: 2, 17, 6899, они образуют число 2176899, которое соответствует маске «21*9».

В ответе укажите первые 5 найденных чисел в порядке возрастания, справа от каждого числа запишите его наибольший простой делитель.
"""
from math import sqrt
import re


def prime_check(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check(n):
    p1 = re.fullmatch("27\d+39\d{1}", n)
    p2 = re.fullmatch("34\d+2\d{1}7", n)
    if p1 is not None or p2 is not None:
        return True
    return False


count = 0
num = 4679001
while count < 5:
    s = []
    t = ''

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            if prime_check(i):
                s.append(str(i))
            k = num // i
            if prime_check(k):
                s.append(str(k))

    s.sort(key=int)
    t = "".join(s)

    if len(t) >= 6 and t[0] in "23":
        if check(t):
            count += 1
            print(num, s[-1])

    num += 1

