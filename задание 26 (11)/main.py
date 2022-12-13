"""
В текстовом файле записан набор натуральных чисел, не превышающих 10^9. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.
"""

with open("26 (8).txt") as f:
    f.readline()
    numbers = list(map(int, f.read().split()))
    numbers.sort()


def binary_search(value, a):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return False
    else:
        return mid


count_pair = 0
max_avg = 0
for i in range(len(numbers) - 1):
    if numbers[i] & 1 == 0:  # Логическое умножение (последний бит умножаем на 1, во всех чёт. числах он равен 0)
        for j in range(i + 1, len(numbers)):
            if numbers[j] & 1 == 0:
                avg = (numbers[i] + numbers[j]) >> 1  # Побитовый сдвиг вправо (деление нацело на 2)
                if binary_search(avg, numbers):
                    count_pair += 1
                    max_avg = max(avg, max_avg)
print(count_pair, max_avg)
