with open("17 (1).txt") as file:
    numbers = [int(elem) for elem in file.read().split()]
count = 0
max_raz = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] - numbers[j]) % 45 == 0 and (numbers[i] % 18 == 0 or numbers[j] % 18 == 0):
            count += 1
            if numbers[i] - numbers[j] > max_raz:
                max_raz = numbers[i] - numbers[j]
print(count, max_raz)