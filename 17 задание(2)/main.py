with open('17 (6).txt') as f:
    numbers = [int(x) for x in f]
    s = []
    for i in range(2, len(numbers)):
        m = [numbers[i], numbers[i - 1], numbers[i - 2]]
        if max(m)**2 < ((numbers[i]**2 + numbers[i-1]**2) or (numbers[i]**2 + numbers[i-2]**2) or (numbers[i-1]**2 + numbers[i-2]**2)):
            s.append(numbers[i] + numbers[i-1] + numbers[i-2])
    print(len(s), max(s))

