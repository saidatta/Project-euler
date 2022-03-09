n, i = 600851475143, 2
while i * i < n:
    while n % i == 0:  # checks for factors.
        n = (n / i)
    i += 1
print(n)
