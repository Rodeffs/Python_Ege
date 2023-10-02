"""
Текстовый файл состоит не более чем из 106 символов L, D и R. Определите длину самой длинной последовательности, состоящей из символов L. Хотя бы один символ L находится в последовательности.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.


"""

with open("zadanie24_2.txt", 'r', encoding="UTF-8") as file:
    data = file.read()
    # Иной способ:
    # data = file.read().replace('R', ' ').replace('D', ' ').split()
    #
    # maxLen = 1
    # for word in data:
    #     if len(word) > maxLen:
    #         maxLen = len(word)
    #
    # print(maxLen)

maxlen = 1
curlen = 1

for i in range(2, len(data)):  # или for i in list(data), разница в том, что в первом случае мы смотрим по индексу
    if data[i] == 'L' and data[i - 1] == data[i]:
        curlen += 1
        if curlen > maxlen:
            maxlen = curlen
    else:
        curlen = 1

print(maxlen)


