'''
Problem Description
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''

#
from lib.euler import gcd

d = 1
numProd, denProd = 1,1
for i in range (1,10):
	for den in range(1,i):
		for num in range(1,den):
			di = num * 10 + i
			denTemp = i * 10 + den
			if num * denTemp == di*den:
				numProd *= num
				denProd *= den

print(denProd/gcd(numProd, denProd))
