def A(n):
    n *= 9
    k = 1
    while pow(10, k, n) != 1:
        k += 1
    return k

DMR_PRIMES = [2, 13, 23, 1662803]

def isPrime(n):#assumes n is odd
    #s, d | 2^s*d = n - 1
    s, d = 0, n - 1
    while d&1 == 0:
        s += 1
        d >>= 1
    for a in DMR_PRIMES:
        if a >= n:
            break
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            for a in range(0, s):
                x = pow(x, 2, n)
                if x == 1:
                    return 0
                if x == n - 1:
                    break
            else:
                return 0
    return 1

n = 5
s = 0
c = 0
while c < 25:
    n += 2
    if n%5 == 0:
        continue
    if (n - 1)%A(n) == 0:
        if not isPrime(n):
            print(n)
            c += 1
            s += n
print(s)

