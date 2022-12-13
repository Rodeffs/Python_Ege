with open('17 (1).txt') as file:
    f = file.read()
    f = list(map(int, f.split()))
count = 0
m = 0
for i in range(10000):
    for j in range(i + 1, 10000):
        if ((f[i] % 160) != (f[j] % 160)) and (f[i] % 7 == 0 or f[j] % 7 == 0):
            count += 1
            if (f[i] + f[j]) > m:
                m = f[i] + f[j]
print(count, m)

with open('17 (1).txt') as f:
    numbers = [int(x) for x in f]
    s = []
    m = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if (numbers[i] % 160 != numbers[j] % 160) and (numbers[i] % 7 == 0 or numbers[j] % 7 == 0):
                s.append(numbers[i] + numbers[j])
                m += 1
    print(m/2, max(s))