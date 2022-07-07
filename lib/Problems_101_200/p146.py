'''
Using basic mod test and checking for euler pseudoprimes to base 4:
(the chances of having so many primes fail the pseudo prime test in a row is fairly small). At the upper bound 150M**2 the results is around 55 bit numbers.  The chances of hitting 1 euler pseudoprime is around 4e-11. Worth the risk to not require a slower miller rabin test, but really not big enough to need sieve theory.


1 (messy) line of python. no libraries, no imports, no memory sieves, no trial division, no miller rabin.

Python
- print sum([n for n in  range(10,150000000,10) if all([pow(2,n**2+x,n**2+x)==2 for x in [1,3,7,9,13,27]]) and
not(pow(2,n**2+21,n**2+21)==2)])



or the unrolled version that is much faster by using continue to abort on first miss and uses mod 210 test upfront
 and escapes to make testing faster:
'''

def epp4(n):
    return not (pow(2, n, n) == 2)


found = []
for s in [10, 80, 130, 200]:
    for n in range(s, 150000000, 210):
        r = n ** 2
        if epp4(r + 1): continue
        if epp4(r + 3): continue
        if epp4(r + 7): continue
        if epp4(r + 9): continue
        if epp4(r + 13): continue
        if epp4(r + 27): continue
        if not (epp4(r + 21)): continue
        found += [n]
        print(n, sum(found))
