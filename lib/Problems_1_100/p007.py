from Euler import is_prime

limit = 10_001
prime_list = [2]
num = 3

while len(prime_list) < limit:
    if is_prime(num):
        prime_list.append(num)
        num += 2
    else:
        num += 2

print(prime_list[-1])