from Euler import prime_sieve

primes = prime_sieve(7081)
LIMIT = 50000000

sums = {0}
for i in range(2, 5):
    newsums = set()
    for p in primes:
        q = p ** i
        if q > LIMIT:
            break
        for x in sums:
            curr_sum = x + q
            if curr_sum <= LIMIT:
                newsums.add(curr_sum)
    sums = newsums
print(str(len(sums)))