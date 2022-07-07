from lib.euler import gcd


def genRadUpToExclusive(n):
    ret = [2, 1] * (n // 2) + ([2] if n & 1 else [])
    ret[0] = 0
    for p in range(3, n, 2):
        if ret[p] == 1:
            for i in range(p, n, p):
                ret[i] *= p
    return ret

def solve(n):
    rad = genRadUpToExclusive(n)
    irad = [[] for _ in range(n)]
    for i in range(1, n):
        irad[rad[i]].append(i)
    ret = 0
    for c in range(1, n):
        t = c // rad[c]
        alim = (c + 1) // 2
        for ra in range(1, t + 1):
            for a in irad[ra]:
                if a >= alim:
                    break
                b = c - a
                if ra * rad[b] < t and gcd(a, b) == 1:
                    ret += c
    print('Answer: %d' % ret)

print(solve(120000))