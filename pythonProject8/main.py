'''
В файле содержится последовательность из 10000 натуральных чисел. Каждое число не превышает 10000. Определите и запишите в ответе сначала количество пар элементов последовательности, у которых различные остатки от деления на d=160 и хотя бы одно из чисел делится на p=7, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

Пример входных данных:

168

7

320

328

Пример выходных данных для приведённого выше примера входных данных:

4 488

Пояснение: Из 4 чисел можно составить 6 пар. В данном случае условиям удовлетворяют пары: 168 и 320, 168 и 7, 320 и 7, 328 и 7. Максимальную сумму дает пара 168 и 320— 488.
'''

with open('17 (3).txt') as f:
    numbers = [int(elem) for elem in f.read().split()]

d = 160
p = 7
count = 0
mxs = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] % d != numbers[j] % d and (numbers[i] % p == 0 or numbers[j] % p == 0):
            count += 1
            if numbers[i] + numbers[j] > mxs:
                mxs = numbers[i] + numbers[j]

print(count, mxs)
