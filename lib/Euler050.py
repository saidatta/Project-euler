import timeit

from Euler import prime_sieve, is_prime

start = timeit.default_timer()
max_prime = 0
L = 1000000
prime_sum = [0]

for p in prime_sieve(L//100):
    prime_sum.append(prime_sum[-1] + p)
    if prime_sum[-1] >= L: break
c = len(prime_sum)

terms = 1
for i in range(c):
    for j in range(c-1, i+terms, -1):
        n = prime_sum[j] - prime_sum[i]
        if j - i > terms and is_prime(n):
            terms, max_prime = j - i, n
            break

print("Project Euler 50 Solution = ", max_prime, " with ", terms, " terms")
stop = timeit.default_timer()
print('Time: ', stop - start)