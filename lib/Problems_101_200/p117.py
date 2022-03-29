# How many ways can a row n units long be filled with:
# - Black squares 1 unit long
# - Red tiles 2 units long
# - Green tiles 3 units long
# - Blue tiles 4 units long
# Denote this quantity as ways[n].
#
# Compute n = 0 manually as a base case.
# Now assume n >= 1. Look at the leftmost item and sum up the possibilities.
# - Black square (n>=1): Rest of the row can be anything of length n-1. Add ways[n-1].
# - Red tile     (n>=2): Rest of the row can be anything of length n-2. Add ways[n-2].
# - Green tile   (n>=3): Rest of the row can be anything of length n-3. Add ways[n-3].
# - Blue tile    (n>=4): Rest of the row can be anything of length n-4. Add ways[n-4].

'''
Tiled this recursively at first, figured out that it was generating OEIS A000078,
then wrote a faster tetra(n) function. My recursive solution is included.


If f(n) is the number of ways to tie a row of n units, then f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4),
where f(0) = 1 and f(n) = 0 for negative n. The reasoning is this: At each step you either place a grey unit, a red unit, a green unit or a blue unit. The solution required memoization.

'''
def compute():
    # Dynamic programming
    LENGTH = 50
    return tetra(LENGTH)

def tile(n,lim):
    count = 0
    if n<lim:
        for t in [1,2,3,4]:
            nn = n
            nn += t
            count += tile(nn,lim)
        return count
    elif n==lim:
        return 1
    else:
        return 0

def tetra(n):
    n += 3
    T = [0,0,0,1]
    for i in range(4,n+1):
        T.append(T[i-1]+T[i-2]+T[i-3]+T[i-4])
    return T[n]

if __name__ == "__main__":
    print(compute())
