import prime
from itertools import permutations

# Pan-digital primes are 4 or 7 digits. Others divisible by 3
for perm in permutations(range(7, 0, -1)):
    num = 0
    for n in perm: num = num * 10 + n
    if prime.is_prime(num):
        print(num)
        break
