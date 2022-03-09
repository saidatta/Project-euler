def divisors(n):
    return list(i for i in range(1, n // 2 + 1) if n % i == 0)


amicable_pair = dict(((n, sum(divisors(n))) for n in range(1, 10000)))
print(
    sum(n for n in range(1, 10000)
        if amicable_pair.get(amicable_pair[n], 0) == n and amicable_pair[n] != n)
)
