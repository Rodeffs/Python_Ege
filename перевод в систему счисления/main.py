"""
Работает только с целыми положительными числами и с системами счисления от 2 до 36
"""


# def in_base(number: int, base: int) -> str:
    # number - число, которое переводим в систему счисления
    # base - система счисления, в которую переводим
    # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # new_number = ''
    # while number != 0:
        # remain = number % base
        # if remain >= 10:
            # new_number = alphabet[remain-10] + new_number
        # else:
            # new_number = str(remain) + new_number
        # number //= base
    # return new_number


print("Enter number to convert into base (must be a natural number): ")
number = int(input())  # Изначальное число
old_number = number

print("Enter base (must be more than 2 and less than 36: ")
base = int(input())  # Система счисления

new_number = ''  # Число в системе счисления

if number >= 0 and 36 >= base >= 2:
    while number != 0:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        remain = number % base
        if remain >= 10:
            new_number = alphabet[remain % 10] + new_number
        else:
            new_number = str(remain) + new_number  # Остаток от деления приписываем слева
        number //= base
    print(old_number, "is", new_number, "in base " + str(base))
else:
    print("Error, invalid entry")
