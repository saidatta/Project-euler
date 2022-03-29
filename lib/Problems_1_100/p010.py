from lib.Euler import is_prime

limit = 2_000_000
# limit = 10
prime_sum = 2
num = 3
while num < limit:
    if is_prime(num):
        prime_sum += num
        num += 2
    else:
        num += 2

print(prime_sum)