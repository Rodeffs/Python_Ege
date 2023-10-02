with open('17 (3).txt') as f:
    numbers = [int(x) for x in f]
    s = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] - numbers[j]) % 2 == 0 and (numbers[i] % 31 == 0 or numbers[j] % 31 == 0):
                s.append(numbers[i] + numbers[j])
    print(len(s), max(s))