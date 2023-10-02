"""
На вход программы поступает последовательность из N натуральных чисел. Рассматриваются все пары различных элементов последовательности, у которых различные остатки от деления на d=160 и хотя бы одно из чисел делится на p=7. Среди таких пар, необходимо найти и вывести пару с максимальной суммой элементов.



Входные данные.

Файл A

Файл B

В первой строке входных данных задаётся количество чисел N (1 ≤ N ≤ 1000). В каждой из последующих N строк записано одно натуральное число, не превышающее 10000. В качестве результата программа должна напечатать элементы искомой пары. Если среди найденных пар максимальную сумму имеют несколько, то можно напечатать любую из них. Если таких пар нет, то вывести два нуля.

Пример организации исходных данных во входном файле:

4

168

7

320

328

Пример выходных данных для приведённого выше примера входных данных:

168 320

В ответе укажите четыре числа: сначала значение искомой пары для файла А (два числа через пробел по возрастанию), затем для файла B (два числа через пробел по возрастанию).
"""
with open("28129_A.txt") as file:
    file.readline()
    numbers = list(map(int, file.read().split()))

max_div_7 = 0
max_not_div_7 = 0
second_div_7 = 0
second_not_div_7 = 0

for number in numbers:
    if number % 7 == 0 and number > max_div_7:
        if second_div_7 % 160 != number % 160:
            second_div_7 = max_div_7
        max_div_7 = number
    elif number % 7 != 0 and number > max_not_div_7:
        if second_not_div_7 % 160 != max_div_7 % 160:
            second_not_div_7 = max_not_div_7
        max_not_div_7 = number

sum1 = max_div_7 + second_div_7
sum2 = max_div_7 + second_not_div_7
sum3 = max_not_div_7 + second_div_7
sum4 = max_not_div_7 + max_div_7

if max(sum1, sum2, sum3, sum4) == sum1:
    if max_div_7 < second_div_7:
        print(max_div_7, second_div_7)
    else:
        print(second_div_7, max_div_7)
elif max(sum1, sum2, sum3, sum4) == sum2:
    if max_div_7 < second_not_div_7:
        print(max_div_7, second_not_div_7)
    else:
        print(second_not_div_7, max_div_7)
elif max(sum1, sum2, sum3, sum4) == sum3:
    if max_not_div_7 < second_div_7:
        print(max_not_div_7, second_div_7)
    else:
        print(second_div_7, max_not_div_7)
elif max(sum1, sum2, sum3, sum4) == sum4:
    if max_not_div_7 < max_div_7:
        print(max_not_div_7, max_div_7)
    else:
        print(max_div_7, max_not_div_7)
