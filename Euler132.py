from math import sqrt

def isprime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(sqrt(n))
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
#########################main method###########

bound = 10**9
sqr_bound = int(bound**.5)
set_items = set()
num = 5 
x = len(set_items)

#for x in range(0,40):
while(len(set_items)<40):
	if((isprime(num)) and (pow(10,bound,num)==1)):
		set_items.add(num)
		x = len(set_items)
	num+=2
	print sum(set_items)

		
