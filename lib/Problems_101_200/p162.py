'''
page 8
Inclusion-exclusion...

Construct a hex string by adding one symbol at a time from left to right. Break the set of all strings of length  into the following subsets and note that they do not intersect, and so the total number of all the strings ( — since leading  is not allowed) is the sum of numbers of elements of these 8 subsets:

1. Strings that do not contain , , and . There are  of them.
2. Strings that contain only one of the the three symbols in question (3 subsets for each symbol).
3. Strings that contain 2 of the symbols, but not the 3d (3 subsets for each symbol excluded).
4. Strings that contain all three symbols.

For each string length we only need to keep track of 4 numbers:
1. The number of strings that contain only  (the number of those that contain only  is the same):
2. The number of strings that contain only  (different, because the leading  is not allowed):
3. The number of strings that contain both  and , but not :
4. The number of strings that contain both  and , but not  (the same as the number of strings that contain both  and , but not ):

For the string of length , obviously, , .

Now it is easy to build the recursion:

,
because by adding any of 15 symbols except  to a string that already contains both  and  one keeps the string in the same subset, and by adding  to a string that contains only 's or vice versa one expands the set of 's and 's.

,
for the same reasons, only the numbers are different because  is always different from .

,
because by adding any of 14 symbols except  and  to a string with 's one keeps it in the same subset. Or one can add  to a string that originally did not contain any of the 3 symbols.

,
again the same reasoning, but different values.

Now that we know the numbers of the "intermediate" 6 sets, we can calculate the "winners", those that contain all the 3 symbols:

.

We also could have used the recursive relation:

,
that is adding any symbol to a "winner" string, or adding  to an  string, or adding  to an  string, or adding  to a  string — all produces a "winner" string of the next order. But using the former non-recursive relationship slightly more efficient computationally.

Now all we need is to run the recursion up to , add all the  up, and convert to hex.

Runs in less than 8 ms in pypy:
'''


nA = 1
n0 = 0
nA1 = 0
nA0 = 0

nwinsum = 0 # sum of "winner" strings of all lengths

for n in range(2,17):
    nA1 = nA1*15 + 2*nA
    nA0 = nA0*15 + nA + n0
    nA = nA*14 + 13**(n-1)
    n0 = n0*14 + 13**(n-1)
    nWIN = 15*16**(n-1) - 13**n - 2*nA - n0 - nA1 - 2*nA0
    nwinsum += nWIN
    print(n, nA, n0, nA1, nA0, nWIN)

print(hex(nwinsum)[2:].upper())