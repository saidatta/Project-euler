from lib import euler

primes = euler.prime_sieve(50)

'''
This can be solved quite elegantly (and quickly) using recursion.

It runs in 15 ms. Most time is spent after the minimum value for n has been found, as the search does not limit how 
often a given prime factor occurs except requiring that it should not be more than the previous and the resulting 
product should be less than the best found so far. So towards the end of the search it even considers 2 ** 53. 
Setting max_a more aggressively can get runtime down to less than one 1ms. There may a smarter, 
adaptive way to terminate the search earlier, but as it runs pretty quicly as is, I did not pursue this. 
'''


def find_best(i=0, max_a=1024, best_sofar=None, ns=1, n=1):
    if ns >= NS:  # Found a better solution
        return n
    p = primes[i]
    for a in range(1, max_a + 1):
        n *= p
        if best_sofar is not None and n > best_sofar:
            break
        best_sofar = find_best(i + 1, a, best_sofar, ns * (a * 2 + 1), n)
    return best_sofar


N = 4000000
NS = N * 2 + 1
print(find_best())
