from lib import euler


primes = euler.prime_sieve(10 ** 5)


def A(curr_prime):
    bit = 2
    remainder = 11
    while remainder != 0:
        remainder = (remainder * 10 + 1) % curr_prime
        bit += 1
    return bit


def check(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    return n == 1


it_can = [11, 17, 41, 73]

for curr_prime in primes:
    # if curr_prime < 100:
    #     continue
    if check(A(curr_prime)):
        print(curr_prime)
        it_can.append(curr_prime)

print(sum(primes) - sum(it_can))
