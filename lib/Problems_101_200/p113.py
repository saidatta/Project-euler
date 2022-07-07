from lib.euler import binomial


def compute():
    DIGITS = 100
    increasing = binomial(DIGITS + 9, 9) - 1
    decreasing = binomial(DIGITS + 10, 10) - (DIGITS + 1)
    flat = DIGITS * 9
    ans = increasing + decreasing - flat
    return str(ans)


if __name__ == "__main__":
    print(compute())
