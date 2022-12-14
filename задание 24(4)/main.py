"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z). Определите максимальное количество идущих подряд символов, среди которых нет ни одной буквы E и при этом не менее трёх букв A.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""
with open("24.txt") as f:
    data = f.read().replace("E", " ").split()

maxlen = 0

for word in data:
    if word.count("A") >= 3 and len(word) > maxlen:
        maxlen = len(word)

print(maxlen)