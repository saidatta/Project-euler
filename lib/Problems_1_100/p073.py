from lib.Euler import gcd

a, b = 3, 2
limit, result = 12000, 0

for d in range(5, limit + 1):
    if(d%1000 == 0):
        print(d)
    for n in range(d // a + 1, (d-1)//b + 1):
        if gcd(n, d) == 1:
            result += 1

print(result)