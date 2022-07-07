#0-9
digit_factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)


def sum_of_digits_factorial(n):
    digit_sum = 0
    while n > 0:
        d = n % 10
        digit_sum = digit_sum + digit_factorials[d]
        n = n // 10
    return digit_sum


print(sum(n for n in range(10, 100000) if n == sum_of_digits_factorial(n)))
