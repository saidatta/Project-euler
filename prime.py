#Hugh Wimberly

"""
Provide functions to generate and test prime numbers.

For better performance, use psycho, another compiler,
sage, or another language.

        
"""

import random
import time

_small_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
_small_prime_set = set(_small_prime_list)

def deterministic_primality_test(n):
    """
    Determine whether n is prime (with certainty)

    Input must be a number
    >>> deterministic_primality_test(3.9)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer

    Numbers less than 2 are not prime.
    >>> deterministic_primality_test(-17) or deterministic_primality_test(1)
    False

    However, 2, 17, and 3592819 are,
    >>> False in [deterministic_primality_test(n) for n in (2, 17, 3592819)]
    False

    while 4, 51, and 12908384294951 are not.
    >>> True in [deterministic_primality_test(n) for n in (4, 51, 12908384294951)]
    False
    
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 101:
        return n in _small_prime_set
    for d in _small_prime_list:
        if n % d == 0:
            return False
    for d in range(101, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True
            

def probablistic_primality_test(n, times=20):
    """
    Determine whether n is prime (with high probablity)

    This function (the Rabin-Miller primality test) may incorrectly
    say a number is prime which is not, but will always be correct
    if it reports a number as composite. times indicates how many
    checks to make: more checks makes the answer more reliable.

    Input must be a number
    >>> probablistic_primality_test(3.9)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer

    Numbers less than 2 are not prime.
    >>> probablistic_primality_test(-17) or probablistic_primality_test(1)
    False

    However, 2, 17, 101, and 3592819 are,
    >>> False in [probablistic_primality_test(n) for n in (2, 17, 101, 3592819)]
    False

    while 4, 153, and 12908384294951 are not.
    >>> True in [probablistic_primality_test(n) for n in (4, 153, 12908384294951)]
    False
    
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 6:
        return deterministic_primality_test(n)
    if n % 2 == 0:
        return False
    
    #n - 1 = d * 2**s, with d odd
    s = 0
    d = n-1
    while d % 2 == 0:
        s += 1
        d //= 2
    for test in range(times):
        x = pow(random.randrange(2, n-2), d, n)
        if x == 1 or x == n-1:
            continue
        for r in range(1, s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                break
        else:
            return False
    return True


def is_prime(n, deterministic=None, tests=20):
    """
    Determine if a number is prime

    The choice between deterministic and probabilistic is probably one
    based on speed, rather than accuracy.

    Basic tests:
    >>> [[is_prime(n, t) for n in (-11, 2, 17, 1324873, 1784789)] for t in (True, False)]
    [[False, True, True, False, True], [False, True, True, False, True]]

    """
    if deterministic == None:
        deterministic = n < 2**22 #seems to be a good cutoff
    if deterministic:
        return deterministic_primality_test(n)
    else:
        return probablistic_primality_test(n, tests)

def primes_between(start, end):
    """
    Yield primes between start and end (inclusive)

    >>> [x for x in primes_between(14333, 14519)]
    [14341, 14347, 14369, 14387, 14389, 14401, 14407, 14411, 14419, 14423, 14431, 14437, 14447, 14449, 14461, 14479, 14489, 14503, 14519]

    """
    if start <= 2:
        yield 2
        start = 3
    if start % 2 == 0:
        start += 1
    for n in range(start, end+1, 2):
        if is_prime(n):
            yield n

def next_smallest_prime(n):
    """Return the smallest prime larger than or equal to n"""
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

_primes = [1] + _small_prime_list #2 is the first prime, not the zeroth
def nth_prime(n):
    """
    Compute the nth prime, attempting to memoize previous results

    >>> nth_prime(100)
    541
    >>> nth_prime(10000) #might take a moment
    104729
    >>> nth_prime(9999) #should be nearly instantaneous
    104723

    """
    while len(_primes) <= n:
        curr = _primes[-1] + 2
        while not is_prime(curr):
            curr += 1
        _primes.append(curr)
    return _primes[n]

def factors(n):
    """
    Reduce n into its prime factors.

    Each factor is returned with the number of times it divides n
    >>> factors(2) == {2:1}
    True
    >>> factors(4356814352345465782) == {2:1, 569:1, 25453:1, 150413845663:1}
    True
    
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    facts = {}
    d = 2
    while n > 1 and not is_prime(n):
        if n % d == 0:
            facts[d] = 0
        while n % d == 0 and n != 0:
            facts[d] = facts[d] + 1
            n = n // d
        d = next_smallest_prime(d+1)
    if n > 1:
        facts[n] = 1
    return facts

def proper_factors(n, include_self=False):
    """Yield all proper factors of n.

    >>> set(proper_factors(28)) == {1, 2, 4, 7, 14}
    True
    >>> set(proper_factors(4942052)) == {1, 2, 4, 19, 38, 76, 65027, 130054, 260108, 1235513, 2471026}
    True

    """
    for product in _subproduct(factors(n)):
        if n != product or n == 1 or include_self:
            yield product

def _subproduct(factor_dict):
    if factor_dict == dict():
        yield 1
    else:
        value, count = factor_dict.popitem()
        for subfact in _subproduct(factor_dict):
            yield subfact
            for p in range(count):
                subfact *= value
                yield subfact

def num_factors(n):
    """
    Return the number of proper factors of n, including 1 and itself.

    >>> num_factors(24)
    8
    """
    num = 1
    for value, count in factors(n).items():
        num *= (count + 1)
    return num
    

def _compare_runtime(n):
    """Measure the runtime of both tests on the number n"""
    t1 = time.time()
    d = is_prime(n, True)
    t2 = time.time()
    p = is_prime(n, False)
    t3 = time.time()
    if p != d:
        raise AssertionError("Primality tests disagree on %d" % n)
    return (t2-t1, t3-t2), p
    
def _test_equivalence(limit=1.0):
    """Test that the primality tests are identical up to t seconds, and report on their runtimes"""
    base, last, = 1, 0.0
    while last < limit:
        x = random.randrange(2**base, 2**(base+1))
        times, prime = _compare_runtime(x)
        deter, prob = (times[0], times[0], times[0]), (times[1], times[1], times[1])
        while prime == False:
            x = random.randrange(2**base, 2**(base+1))
            times, prime = _compare_runtime(x)
            deter = min(deter[0], times[0]), max(deter[1], times[0]), deter[2] + times[0]
            prob = min(prob[0], times[1]), max(prob[1], times[1]), prob[2] + times[1]
            
        print(base, deter[2], prob[2]) 
        last = max(deter[1], prob[1])
        base += 1
        
#import doctest
#doctest.testmod()
