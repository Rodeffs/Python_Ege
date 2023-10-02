'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
with open("24_demo (1).txt") as f:
    dat = f.read()

curlen = 0
maxlen = 0

for i in range(1, len(dat)):
    if dat[i] == "Y" and dat[i - 1] == "X" or \
            dat[i] == "Z" and dat[i - 1] == "Y" or \
            dat[i] == "X" and dat[i - 1] == "Z":
        curlen += 1
        if curlen > maxlen:
            maxlen = curlen
    elif dat[i] == "X":
        curlen = 1
    else:
        curlen = 0

print(maxlen)
