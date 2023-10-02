from math import sqrt


# with open("zadanie_24.txt") as f:
#     B = f.read().replace("A", " ").replace("C", " ").split()
#     print(len(max(B)))

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for j in range(2, int(sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True


count = 1
for i in range(45006, 50222):
    if i % 100 == 19:
        if is_prime(i):
            print(count, i)
            count += 1
