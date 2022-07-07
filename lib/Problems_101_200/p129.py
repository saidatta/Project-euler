import time

from lib.euler import gcd

start_time = time.time()

def R(k):    # Only required for testing
    ch = '1'
    srep = ''
    for i in range(k):
        srep += ch
    return int(srep)


def A(n):    # Only required for testing
    if gcd(n,10) > 1:
        return -1
    k = 2
    while True:
        if R(k) % n == 0:
            return k
        k += 1

'''
 Make use of: 
 1) R(k) = (10^k - 1)/9
 2) R(k+l) = 10^l R(k) + R(l) or for l = 1: R(k+1) = 10*R(k) + 1
 3) if R(k) = n*m + r => R(k+1) = 10*R(k) + 1 = 10*(n*m+r)+1 = 10*n*m + 10*r + 1 and
    R(k+1) % n = 10*r + 1 => keeping remainder is sufficient for A(n)
 4) Observed that: A(n) <= n so A(n) exceeds 10^6 for n >= 10^6
'''

kstop = 10**6
n = 10**6 - 7    # start search just below kstop
while True:
    n += 2    # only odd n
    if gcd(n,10) == 1:
        k = 2        # keep track of k
        rest = 11    # start with R(k=2) and increase k to find first k for which R(k) % n = 0
        while True:
            rest = rest % n    # remainder multiple of n?
            if rest == 0:
                if k > kstop:    # solution found!
                    print(("\nA(%d) = %d") %(n,k))
                    print("> %s seconds <" %(time.time() - start_time))
                    exit()
                break
            else:
                k += 1                # try k+1
                rest = 10*rest + 1    # only compute remainder for k+1
