with open("24_demo (2).txt") as file:
    data = file.read().replace("Z", " ").replace("Y", " ").split()
    maxlen = 1
    for i in data:
        if len(i) > maxlen:
            maxlen = len(i)

print(maxlen)


