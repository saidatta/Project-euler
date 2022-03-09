import prime

for n in range(1, 1_000_000):
    Tn = (n * (n + 1)) // 2
    # coprime factoriziation
    if n % 2 == 0:
        count = prime.num_factors(n // 2) * prime.num_factors(n + 1)
    else:
        count = prime.num_factors(n) * prime.num_factors((n + 1) // 2)

    if count >= 500:
        print(Tn)
        break