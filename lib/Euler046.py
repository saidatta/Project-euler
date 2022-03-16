from Euler import is_prime, prime_sieve
MAX = 10000
squares = dict.fromkeys((x*x for x in range(1, MAX)), 1)
prime_list = prime_sieve(MAX)
for x in range(35, MAX, 2):
    if not is_prime(x):
        is_goldbach = 0
        for p in prime_list[1:]:
            if p >= x: break
            if (x - p)/2 in squares:
                is_goldbach = 1
                break
        if not is_goldbach:
            print(x)
            break