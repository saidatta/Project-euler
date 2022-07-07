'''
A slight modification of the function from problem 114: replacing the length 3 by . This is pretty much it: afterwards
I just checked that for 200 the value is already past one million and then looked at the values from 150 to 200.
Runs close to instantly because of memoization.
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def BlockComb(n, m):
    if n < m: return 1 # 0 is also 1 combination
    else:
        summa = 1 + BlockComb(n-1,m) # all combinations for one additional grey tile
        for k in range(m+1,n+1): # if the additional tile is red, that means at least an m-long color bar plus 1 grey tile
            summa += BlockComb(n-k,m)
        return summa

for N in range(150,201):
    print(N, BlockComb(N,50))