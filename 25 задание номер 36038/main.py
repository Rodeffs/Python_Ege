def FM(a):
    ls = [i for i in range(2, a) if a % i == 0]
    if ls:
        return max(ls) + min(ls)
    else:
        return 0


start = 452022
count = 0

while count != 5:
    M = FM(start)
    if M % 7 == 3:
        count += 1
        print(start, M)
    start += 1
