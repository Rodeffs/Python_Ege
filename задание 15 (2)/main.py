for A in range(64): # это для наибольшего целого А
    B = True
    for x in range(64):
        if (x & 51 == 0 or x & 41 != 0 or x & (63 - A) == 0) == 0:
            B = False
    if B:
        print(63 - A)
        break
