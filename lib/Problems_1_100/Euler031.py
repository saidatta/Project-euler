'''
	This code basically loops through the coins array.
	and 2nd loop is for the calculating it to 200.
	This. will give you the number of ways but it does not provide you with
	the optimal solution.
'''

target = 200
coins = [1,2,5,10,20,50,100,200]

ways = [1]+[0]*target

for c in coins:
	for i in range(c, target+1):#c to 200.
		ways[i] += ways[i-c]
print(ways[target])
