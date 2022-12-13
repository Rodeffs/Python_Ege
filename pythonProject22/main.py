
    if y > x: # меняем местами x и y
        z = x
        x = y
        y = z
    a = x # наибольшее из x и y
    b = y # наименьшее
    while b > 0:
        r = a % b
        a = b
        b = r
