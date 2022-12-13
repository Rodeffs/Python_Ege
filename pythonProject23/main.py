def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return F(n//2) + 1
    return F(n-3) + 3


count = 0
for i in range(1, 100001):
    if F(i) == 12:
        count += 1

print(count)
