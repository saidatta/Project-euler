def digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += (n % 10)
        n //= 10
    return sum_digits


print(digits(pow(2, 1000)))
