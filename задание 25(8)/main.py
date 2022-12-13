"""
Найдите все натуральные числа N, принадлежащие отрезку [400000000;600000000], которые можно представить в виде N=2^m·3^n, где m — чётное число, n — нечётное число. В ответе запишите все найденные числа в порядке возрастания.
"""
import threading


def F(start, stop):
    for i in range(start, stop + 1):
        N = i
        m = 0
        n = 0
        while N % 2 == 0:
            m += 1
            N /= 2

        while N % 3 == 0:
            n += 1
            N /= 3

        if m % 2 == 0 and n % 2 == 1 and pow(2, m) * pow(3, n) == i:
            print(i)

    return 0


def main():
    thr1 = threading.Thread(target=F, args=(400000000, 450000000,))
    thr1.start()
    thr2 = threading.Thread(target=F, args=(450000001, 500000000,))
    thr2.start()
    thr3 = threading.Thread(target=F, args=(500000001, 550000000,))
    thr3.start()
    thr4 = threading.Thread(target=F, args=(550000001, 600000000,))
    thr4.start()

    return 0

    # Это мультипоточность, благодаря ей программа выполнится быстрее


main()
