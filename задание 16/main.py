def F(n):
        if n == 0:
                return 0
        if n % 2 == 0 and n > 0:
                return F(n/2)
        return 1 + F(n-1)

n = 0
while True:
        x = F(n)
        if x == 11:
                print(n)
                break
        n += 1