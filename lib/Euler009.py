def brute_force():
    a, b, c = 0, 0, 0
    perimeter, found = 1000, False
    # since  a < b < c the upper bounds are as follows.
    for a in range (1, perimeter // 3):
        for b in range (a, perimeter // 2):
            c = perimeter - a - b
            if (a * a + b * b == c * c):
                found = True
                break

        if (found):
            break

    return a * b * c

print (brute_force())


