# int aMax = 0, bMax = 0, nMax = 0;
# int[] primes = ESieve(87400);
#
# for (int a = -1000; a <= 1000; a++) {
# for(int b = -1000; b <= 1000; b++){
# int n = 0;
# while (isPrime(Math.Abs(n * n + a * n + b))) {
# n++;
# }
# if (n > nMax) {
# aMax = a;
# bMax = b;
# nMax = n;
# }
# }
# }

from Euler import is_prime, prime_sieve

primes = prime_sieve(87400)
nMax, aMax, bMax = 0,0,0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while(is_prime(abs(n*n + a*n + b))):
            n += 1
        if n > nMax:
            aMax, bMax, nMax = a, b, n

print(aMax * bMax)