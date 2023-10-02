"""Пузырьковая сортировка"""
# Функция получает на вход список и выводит также список.
# Данная сортировка сортирует от меньшего к большему


def bubble_sort(ls: list) -> list:
    length = len(ls)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if ls[j] <= ls[i]:
                ls[j], ls[i] = ls[i], ls[j]
    return ls


#           if ls[i] <= ls[j]:
#               ls[j], ls[i] = ls[i], ls[j] - это для сортировки от большего к меньшему

"""Быстрая сортировка"""


# def partition(ls: list, Left: int, Right: int):
#     R = ls[Right]
#     i = Left - 1
#     for j in range(Left, Right):
#         if ls[j] <= R:
#             i += 1
#             ls[i], ls[j] = ls[j], ls[i]
#     ls[i + 1], ls[Right] = ls[Right], ls[i + 1]
#     return i + 1
#
#
# def quick_sort(ls: list, Left: int, Right: int) -> list:
#     if Left < Right:
#         mid = partition(ls, Left, Right)
#         quick_sort(ls, Left, mid - 1)
#         quick_sort(ls, mid + 1, Right)

def quick_sort(ls: list, start: int, end: int) -> list:
    if start >= end:
        return

    mid = (start + end) // 2
    sample = ls[mid]
    L = start
    R = end

    while L <= R:

        while ls[L] < sample:
            L += 1

        while ls[R] > sample:
            R -= 1

        if L <= R:
            ls[L], ls[R] = ls[R], ls[L]
            L += 1
            R -= 1

    quick_sort(ls, start, R)
    quick_sort(ls, L, end)




