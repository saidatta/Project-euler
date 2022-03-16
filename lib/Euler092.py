def compute():
    ans = sum(1 for i in range(1, 10_000_000) if get_terminal(i) == 89)
    return str(ans)


TERMINALS = (1, 89)


def get_terminal(n):
    while n not in TERMINALS:
        n = square_digit_sum(n)
    return n


def square_digit_sum(n):
    result = 0
    while n > 0:
        result += SQUARE_DIGITS_SUM[n % 1_000]
        n //= 1000
    return result


SQUARE_DIGITS_SUM = [sum(int(c) ** 2 for c in str(i)) for i in range(1_000)]

if __name__ == "__main__":
    print(compute())
