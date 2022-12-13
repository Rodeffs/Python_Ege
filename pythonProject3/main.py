A = 0
while True:
    B = True
    for x in range(32):
        if (x & 29 == 0 or x & 12 != 0 or x & A != 0) == 0:
            B = False
    if B:
        print(A)
        break
    A += 1
