"""
Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""
with open("zadanie24_1.txt") as file:
    data = file.read()

curlen = 1
maxlen = 1

for i in range(1, len(data)):
    if data[i] != data[i - 1]:
        curlen += 1
        if curlen > maxlen:
            maxlen = curlen
    else:
        curlen = 1

print(maxlen)