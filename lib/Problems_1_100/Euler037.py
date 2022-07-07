import itertools

from lib import euler

TOTAL_NUM_TRUNCATABLE_PRIMES = 11
STARTING_NUM = 10
def compute():
    # find truncatable prime by incrementing from STARTING_NUM until we reach TOTAL_NUM_TRUNCATABLE_PRIMES.
    ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(STARTING_NUM)), TOTAL_NUM_TRUNCATABLE_PRIMES))
    return str(ans)


def is_truncatable_prime(n):
    # Test if left-truncatable
    i = 10
    x = n
    while i <= n:
        if not Euler.is_prime(n % i):
            return False
        i *= 10

    # Test if right-truncatable
    while n > 0:
        if not Euler.is_prime(n):
            return False
        n //= 10

    print(x)
    return True


if __name__ == "__main__":
    print(compute())
