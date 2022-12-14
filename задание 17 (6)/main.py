"""
В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 60, затем максимальную из разностей элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
"""
with open("17 (7).txt") as f:
    numbers = list(map(int, f.read().split()))

count = 0
max_dif = 0
for i in range(0, 9999):
    for j in range(i+1, 10000):
        dif = numbers[i] - numbers[j]
        if dif % 60 == 0:
            count += 1
            max_dif = max(max_dif, dif)
print(count, max_dif)
