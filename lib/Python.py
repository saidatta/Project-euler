
def isPalindromic(z):
	return str(z)==str(z)[::-1]

bound = 10**8
sqr_bound = int(bound**.5)#square rooting the limit.Because it is a palindrome.
set_items = set()
j=0
for x in range(1,sqr_bound):
	i = x*x
	for y in range(x+1,sqr_bound):
		i += y*y
		if(i>=bound):
			break
		if(isPalindromic(i)):
			set_items.add(i)
print(sum(set_items), len(set_items))

