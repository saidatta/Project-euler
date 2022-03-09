
def isPalindromic(str):
	return str(n)==str(n)[::-1]

bound = 10**8
sqr_bound = int(bound**.5)#square rooting the limit.Because it is a palindrome.
set_items = set()

for x in range(1,bound):
	i = x*x
	for y in range(i+1,bound):
		j = y*y
		if(j>=bound):
			break
		if(isPalindromic(j)):
			set_items.add(j)
print "%d", sum(j)

