"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых не более одной буквы D.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""
with open("24_1.txt", mode="r", encoding="UTF-8") as f:
    content = f.read()

count_D = 0
max_len = 0
count = 0
index_D = 0
for i in range(len(content)):
    if not content[i] == "D":
        count += 1
        if max_len < count: max_len = count

    elif count_D == 0:
        count_D = 1
        count += 1
        index_D = i
        if max_len < count: max_len = count

    elif count_D == 1:
        count = i - index_D
        index_D = i
        if max_len < count: max_len = count

print(max_len)