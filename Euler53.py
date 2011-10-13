
from Euler import binomial
limit, maxn, c = 1e6, 100, 0
 
for n in range(23, maxn+1):
  for r in range(2, n/2+1):
    if binomial(n, r) > limit:
      c += n + 1 - 2*r
      break
print "Answer to PE53 = ", c
