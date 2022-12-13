# with open("17 (4).txt") as file:
#     data = [int(x) for x in file]
#     numbers = []
#     count = 0
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if (data[i] + data[j]) % 117 == 0:
#                 numbers.append(data[i] + data[j])
#                 count += 1
#     print(count, max(numbers))

def f(n):
    delit = []
    for i in range(2, n+1):
        if n % i == 0 and i % 2 == 0:
            delit.append(i)
    if len(delit) == 4:
        return delit
    return 0


for i in range(110203, 110246):
    t = f(i)
    if t:
        print(*t)

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.

Например, в тексте CBCABABACCC есть комбинации CBC, ABA (два раза), BAB и CCC. Чаще всего— 3 раза— между двумя одинаковыми символами стоит B, в ответе для этого случая надо написать B.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""

# with open("24 (1).txt") as file:
#     data = file.read()
#     letters = []
#     count = 1
#     for i in range(len(data)-2):
#         if data[i] == data[i + 2]:
#             letters.append(data[i+1])
#     for j in range(len(sorted(letters))):
#         if letters[j] == letters[j+1]:
#             count += 1
#
#
