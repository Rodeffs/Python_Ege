def Is_Prime(n):
    from math import sqrt
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(2, int(sqrt(n)) + 1): # проверяем до корня из числа + 1, т.к. после этого делилители будут повторяться
        if n % i == 0:
            return False

    return True

