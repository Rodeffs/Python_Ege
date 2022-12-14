"""
В лесничестве саженцы сосны высадили параллельными рядами, которые пронумерованы идущими подряд натуральными числами. Растения в каждом ряду пронумерованы натуральными числами начиная с единицы.

По данным аэрофотосъёмки известно, в каких рядах и на каких местах растения не прижились. Найдите ряд с наибольшим номером, в котором есть ровно 13 идущих подряд свободных мест для посадки новых сосен, таких, что непосредственно слева и справа от них в том же ряду растут сосны. Гарантируется, что есть хотя бы один ряд, удовлетворяющий этому условию. В ответе запишите два целых числа: наибольший номер ряда и наименьший номер места для посадки из числа найденных в этом ряду подходящих последовательностей из 13 свободных мест.

В первой строке входного файла находится число N — количество прижившихся саженцев сосны (натуральное число, не превышающее 20 000). Каждая из следующих N строк содержит два натуральных числа, не превышающих 100 000: номер ряда и номер места в этом ряду, на котором растёт деревце.

Выходные данные

Два целых неотрицательных числа: наибольший номер ряда и наименьший номер места в выбранной последовательности из 13 мест, подходящих для посадки новых сосен.

Типовой пример организации входных данных

7

40 3

40 7

60 33

50 125

50 129

50 68

50 72

Для приведённого примера, при условии, что необходимо 3 свободных места, ответом является пара чисел: 50; 69.

Типовой пример имеет иллюстративный характер. Для выполнения задания используйте данные из прилагаемых файлов.
"""

with open("107_26.txt") as file:
    N = int(file.readline())
    coord = (content.strip("\n").split() for content in file.readlines())  # Читаем файл, заносим координаты в матрицу
    coord = map(lambda x: (int(x[0]), int(x[1])), coord)  # Делаем эти значения целочисленными



