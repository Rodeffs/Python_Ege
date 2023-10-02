"""
В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар нечётных чисел, что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.

Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк содержит одно число.

В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
"""
with open("26 (2).txt") as file:
    N = int(file.readline())
    data = list(map(int, file.read().split()))
data.sort()


def binary(val, ls):
    low = 0
    high = len(ls) - 1
    mid = (low + high) // 2
    while val != ls[mid] and low <= high:
        if val > ls[mid]:
            low = mid + 1
        elif val < ls[mid]:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return False
    return True


max_arif = 0
count = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] % 2 != 0 and data[j] % 2 != 0:
            s = (data[i] + data[j]) // 2
            if binary(s, data):
                count += 1
                if s > max_arif:
                    max_arif = s
print(count, max_arif)
