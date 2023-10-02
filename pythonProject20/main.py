def partition(ls: list, Left: int, Right: int):
    R = ls[Right]
    i = Left - 1
    for j in range(Left, Right):
        if ls[j] <= R:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[i + 1], ls[Right] = ls[Right], ls[i + 1]
    return i + 1


def quick_sort(ls: list, Left: int, Right: int) -> list:
    if Left < Right:
        mid = partition(ls, Left, Right)
        quick_sort(ls, Left, mid - 1)
        quick_sort(ls, mid + 1, Right)


lst = [2, 5, 8, 4824948, 0, 214, 4567, 24368, 3, 8]
quick_sort(lst, 0, len(lst) - 1)
print(lst)