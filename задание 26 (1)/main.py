"""
В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.

Входные данные.

Задание 26

Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк содержит одно число.

В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
"""
with open("26 (1).txt") as file:
    n = int(file.readline())
    data = list(map(int, file.read().split()))
data.sort()


def binary(value, ls):
    low = 0
    mid = len(ls) // 2
    high = len(ls) - 1
    while ls[mid] != value and low <= high:
        if value > ls[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return False
    else:
        return True


max_bin = 0
count_bin = 0

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] % 2 == 0 and data[j] % 2 == 0:
            temp_bin = (data[i] + data[j]) // 2
            if binary(temp_bin, data):
                count_bin += 1
                if temp_bin > max_bin:
                    max_bin = temp_bin

print(count_bin, max_bin)
