'''
В файле содержится последовательность из 10000 целых положительных чисел.
Каждое число не превышает 10 000.
Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 8,
затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два различных элемента последовательности.
 Порядок элементов в паре не важен.
'''

with open("17 (2).txt", "r") as file:
    digits = [int(elem) for elem in file.read().split()]

count = 0
max_sum = 0
for i in range(len(digits) - 1):
    for j in range(i + 1, len(digits)):
        if (digits[i] + digits[j]) % 8 == 0:
            count += 1
            if (digits[i] + digits[j]) > max_sum:
                max_sum = (digits[i] + digits[j])

print(count, max_sum)