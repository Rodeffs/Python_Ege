"""
Работает только с целыми положительными числами и с системами счисления от 2 до 36
"""


def in_base(number: int, base: int) -> str:
    # number - число, которое переводим в систему счисления
    # base - система счисления, в которую переводим
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_number = ''
    while number != 0:
        remain = number % base
        if remain >= 10:
            new_number = alphabet[remain-10] + new_number
        else:
            new_number = str(remain) + new_number
        number //= base
    return new_number
