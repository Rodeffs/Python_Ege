def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    return 1 + F(n - 1)


for n in range(1, 901):
    if F(n) == 9:
        print(n)

# или другой способ:

count = 0
for n in range(1, 901):
    if F(n) == 9:
        count += 1
print(count)
