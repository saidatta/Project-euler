import math
from functools import reduce
from math import sqrt, ceil
import random


# Tests whether x is a perfect square, for any integer x.
def is_square(x):
    if x < 0:
        return False
    y = sqrt(x)
    return y * y == x

def factorial(n): return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def is_perm(a, b): return sorted(str(a)) == sorted(str(b))


def is_palindromic(n): return str(n) == str(n)[::-1]


def is_pandigital(n, s=9): n = str(n);return len(n) == s and not '1234567890'[:s].strip(n)

def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result

def digits(n):
    return list(map(int, str(n)))

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


# Copyright (c) 2010 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?action=history&offset=20101013093632
def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n % p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7;
    i = 1
    while m <= bound and m * m <= n:
        if n % m == 0:
            return m
        m += dif[i % 8]
        i += 1
    return n


def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n % p == 0:
            e += 1;
            n /= p
        F.append((p, e))
    F.sort()
    return F


def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    if b == 0: return a
    while b != 0:
        (a, b) = (b, a % b)
    return a


def perm(n, s):
    if len(s) == 1: return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + perm(r, s[:q] + s[q + 1:])

def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def prime_sieve(end):
    assert end > 0, "end must be >0"
    lng = ((end // 2) - 1 + end % 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end - 1) / 4.0)), 0, 4
    for xd in range(4, 8 * x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end - 1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4 - 8 * (1 - end))) / 4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x * x + x) << 1) - 1, (((x - 1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[:max(0, end - 2)]

    for n in range(5 >> 1, (int(sqrt(end)) + 1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s = int(sqrt(end)) + 1
    if s % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes

def from_digits(digits):
    n = 0
    for digit in digits:
        n *= 10
        n += digit
    return n


def permute_factors_in_powers(n, power_pattern, factors,
                              repeats=False, depth=1,
                              factor_start=0, used=None):
    """If power_pattern is 2, 1, 1, iterate every value of a^2*b*c <= n
    where a, b, c are from sliceable factors"""
    if used is None:
        used = set()
    for fi, factor in enumerate(factors[factor_start:], start=factor_start):
        # print(" "*depth + str(factor), sorted(used))
        if not repeats and factor in used:
            # print(" "*depth + str(factor), sorted(used), "breaking out!")
            continue
        my_power = power_pattern[0]
        my_contrib = factor ** my_power
        if my_contrib > n:
            break
        # print(" "*depth + str(my_contrib), sorted(used))
        if len(power_pattern) == 1:
            yield my_contrib
        else:
            remaining = n // my_contrib
            rem_power_pattern = power_pattern[1:]
            if rem_power_pattern[0] == my_power:
                if repeats:
                    next_factor_start = 0
                else:
                    next_factor_start = fi+1
            else:
                next_factor_start = 0
            hits = False
            used.add(factor)
            for val in permute_factors_in_powers(
                    remaining, rem_power_pattern, factors, repeats,
                    depth+1, next_factor_start, used):
                yield my_contrib * val
                hits = True
            used.remove(factor)
            if not hits:
                break