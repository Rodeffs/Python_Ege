"""
(№ 4073) (В. Шелудько) Значение выражения 7^2103 – 6∙7^1270 + 3∙7^57 – 98 записали в системе счисления с основанием 7. Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной системе счисления.
"""
number = pow(7, 2103) - 6 * pow(7, 1270) + 3 * pow(7, 57) - 98
base = 7


def sept(n):
    new_number = ''
    while n > 0:
        new_number = str(n % base) + new_number
        n //= base
    return new_number


new_number = sept(number)

answer = 0
for i in list(new_number):  # list преобразует строку в список
    answer += int(i)

print(answer)
