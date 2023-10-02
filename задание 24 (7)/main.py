"""
Текстовый файл состоит не более, чем из 107 строчных букв английского алфавита. Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""
with open("24 (4).txt") as file:
    data = file.read().replace("ad", "a d").replace("da", "d a").split()
# length = 0
# max_length = 0
# for i in range(len(data)):
#     length = len(data[i])
#     if length > max_length:
#         max_length = length
# print(max_length)

print(len(max(data, key=len)))