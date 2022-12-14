"""
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210 235;210300], числа, имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.

Например, в диапазоне [10;16] ровно четыре различных натуральных делителя имеет число 12, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

2 3 4 6
"""


def check(n):
    numbers = []
    for i in range(2, n // 2 + 1):
        if i % 2 == 0:
            if n % i == 0:
                numbers.append(i)
    if len(numbers) == 4:
        return numbers
    return 0


for i in range(110203, 110246):
    num = check(i)
    if check(i):
        print(*num)  # * распаковывает список и выдаёт значения в нём
