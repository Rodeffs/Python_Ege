with open("17.txt", "r") as f:
    cont = f.read().split()  # читает файл и делит их на отдельные символы
    digits = [int(elem) for elem in cont]  # элементы становятся целочисленными значениями из списка cont

max_sum = 0
count = 0
for i in range(len(digits) - 2):

    x = digits[i]
    y = digits[i+1]
    z = digits[i+2]

    c = max(x, y, z)
    a = min(x, y, z)
    b = x+y+z - (a+c)

    if c**2 == a**2 + b**2:
        count += 1
        if x + y + z > max_sum:
            max_sum = x + y + z

print(count, max_sum)