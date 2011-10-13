from math import factorial

def f_d(n, d):#factorial division.
    if n < d:
        return 0
    if n == d:
        return 1
    return n*f_d(n-1, d)

def binomial(n,m):
 if n < m :
       	return 0
 if m > n-m:
       	return f_d(n, m)//factorial(n-m)
 return f_d(n, n-m)//factorial(m)

number = 5

result = binomial(number+10,10) + binomial(number+9,9) - 10*number - 2

print"Result1:", result
## When working with a very large number n, the bouncy set B less than n is 
## much larger than B', all non-bouncy numbers less than n. So, we count the
## non-bouncy numbers in our solution. The non bouncy set is equal to the
## union of the sets of Increasing and Decreasing numbers. B' = I U D.
## If one starts manually counting the number of increasing or decreasing 
## numbers for any number of digits, it becomes obvious that there is a 
## pattern. The number of decreasing numbers of length d and starting digit n
## can be found using the combinatorial function: nCr(n+(d-1), d-1). A
## similar function for increasing numbers also exists: nCr((9-n)+(d-1), d-1)
## If we think about it, finding all of the decreasing numbers starting with
## a certain digit n is similar to selecting combinations of digits from a 
## restricted set--numbers less than n. This realization is enough to make
## our algorithm so efficient that it takes less than a second. However,
## if you start following the counts of all increasing and decreasing numbers
## for numbers with a given number of digits, you will find that they also
## follow a combinatorial pattern. Following this, as you might expect,
## the sum of all of the increasing and decreasing numbers up to a given
## number of digits can be expressed using single combinatorial functions.
## Once you have the numbers of increasing and decreasing numbers, you must
## simply remove the intersection of the two sets from your total.
## 
## This file shows both my initial method for solving the problem, by adding
## increasing and decreasing numbers on a per-digit, per-num-digits basis
## (which uses a few thousand iterations) and a solution with single nCrs
## (which uses <100 iterations).
#from EulerTools import nCr

## The more  intuitive run through the problem.
## Produces the same results as the crunched version below
#nonbnc = 0
#for d in range(1,101):
#       nonbnc+=1
#       for n in range(d, d+8):
#               nonbnc+= 2*nCr(n,d-1)
#       nonbnc+=nCr(d+8,d-1)
#       nonbnc-=9
#print(nonbnc)

nonbnc = 0
for r in range(0,100):
    for n in range(r+1, r+9):
        nonbnc+= 2*binomial(n,r)
    nonbnc+=binomial(r+9,r)
    nonbnc-=8
print("Non bouncys:",nonbnc)

print(binomial(110,10) + binomial(109,9) - 10*100 - 2)
