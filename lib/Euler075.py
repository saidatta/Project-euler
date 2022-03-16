"""
This is just an extension of Problem 9 of project euler.
I just initiated the value, then took a squareroot( since the values req. are 3)
Then did a gcd b/w the 2 values to find the later value.
Then did a sum to get the Length. Then added them and printed them out.
"""

from Euler import gcd, sqrt
 
L = 1500000
sqrt_L = int(sqrt(L))
lengths = [0]*L # initating the arrays.
for i in range(1, sqrt_L, 2):
  for j in range(2, sqrt_L- i , 2):
      if gcd(i, j) == 1: 
           sum = abs(j*j - i*i) + 2*i*j + i*i + j*j
           for solution_ans in range(sum, L, sum):
                lengths[solution_ans]+=1

print(lengths.count(1))
