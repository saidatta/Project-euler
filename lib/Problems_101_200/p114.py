from functools import lru_cache

'''

So, what exactly happens here? The basic seed values are easy: for cases N-1  and 2  there is only one solution.
 It is not so easy to understand though, that we need yet one more: for N=0  there is also 1 solution (see below).
  For N > 3 we start the recursion. When we increase the size, we have 2 options: either we add a grey tile and 
  then the number of combinations is simply for the size N-1 or it is a red tile. Of course the red tile cannot exist alone, 
  so this opens the main can of worms. I consider two basic cases: 1. The red tile is a part of the huge bar covering 
  the whole thing. This adds just one solution for any case starting from N=3. 2. The red tile is a part of a smaller bar.
   But this smaller bar can only exist with other combinations if it has a grey tile affixed next to it ensuring the 
   required buffer zone. So we must remove the length of at least 4 out of consideration and consider all combinations
    beyond it. This happens for the first time when N = 4 . But "all combinations beyond it" in this case correspond to the 
    case N = 0, that's why we need a seed value of  for that one too.

This is how it works e. g. for the toy case of N = 7: 1 for the whole length of 7 covered in red plus all combinations 
for N=6  (that is 11). Case 3-long bar with a grey tile attached: all combinations for  7-4=3, that is 2. 
Case 4-long bar with a grey
  tile attached: all combinations for,7-5=2 that is 1. Case 5-long bar with a grey tile attached: all combinations for 
  7-6=1, also 1. Finally, case 6-long bar with a grey tile attached: all combos for 7-7=1, another 1. Total is 1+11+2+1+1+1=15 .
   It is a bit crazy (it would have been MUCH more beautiful without that additional grey tile and if all sizes of bars
    starting from m=2  were permitted!), but it works.
'''
@lru_cache(maxsize=None)
def BlockComb(n):
    if n < 3: return 1 # 0 is also 1 combination
    else:
        summa = 1 + BlockComb(n-1) # all combinations for one additional grey tile
        for m in range(4,n+1): # if the additional tile is red, that means at least a 3-long color bar plus 1 grey tile
            summa += BlockComb(n-m)
        return summa

print(BlockComb(50))