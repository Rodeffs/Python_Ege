"""
Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000], которые можно представить в виде N = 2m•7n, где m – чётное число, n – нечётное число. В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n.
"""

m, n = 0, 1
ls = []
N = pow(2, m) * pow(7, n)

while N < 300000000:
    # Сначала переберем значения для n, потом для m
    while N < 100000000:  # Добираем до 100000000, увеличивая n
        n += 2
        N = pow(2, m) * pow(7, n)
    while 100000000 <= N <= 300000000:  # Перебираем все n
        ls.append((N, m+n))
        n += 2
        N = pow(2, m) * pow(7, n)
    m += 2  # Теперь увеличиваем m и начинаем перебирать по новой для n
    n = 1
    N = pow(2, m) * pow(7, n)

print(*sorted(ls), sep="\n")
