from lib.Euler import list_primality

def compute():
    LIMIT = 10_000
    isprime = list_primality(LIMIT - 1)
    for base in range(1000, LIMIT):
        if isprime[base]:
            for step in range(1, LIMIT):
                secondNum = base + step
                thirdNum = secondNum + step
                if secondNum < LIMIT and isprime[secondNum] and has_same_digits(secondNum, base) \
                        and thirdNum < LIMIT and isprime[thirdNum] and has_same_digits(thirdNum, base) \
                        and (base != 1487 and secondNum != 4817):
                    return str(base) + str(secondNum) + str(thirdNum)
    raise RuntimeError("Not found")


def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))

if __name__ == "__main__":
    print(compute())
