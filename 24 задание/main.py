with open("24_demo.txt") as f:
    data = f.read().replace("X", " ").replace("Z", " ").split()

maxlen = 1

for i in data:
    if len(i) > maxlen:
            maxlen = len(i)

print(maxlen)