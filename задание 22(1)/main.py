"""
Ниже записана программа, которая вводит натуральное число x, выполняет преобразования, а затем выводит два числа. Укажите наименьшее возможное значение x, при вводе которого программа выведет числа 5 и 16.
x = int(input())
m = 0
s = 0
while x > 0:
  d = x % 6
  s += d
  if d > m: m = d
  x = x // 6
print(m,s)
"""
x = 0
while True:
    x1 = x
    m = 0
    s = 0
    while x1 > 0:
        d = x1 % 6
        s += d
        if d > m: m = d
        x1 = x1 // 6
    if m == 5 and s == 16:
        print(x)
        break
    x += 1
