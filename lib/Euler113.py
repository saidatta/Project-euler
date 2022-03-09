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


##number = 5 --- not exactly working.

##result = binomial(number+10,10) + binomial(number+9,9) - 10*number - 2

##print"Result1:", result
##########################################################################

nonbnc = 0
num = 100
for i in range(0,num):
    for j in range(i+1, i+9):
        nonbnc= 2*binomial(j,i) + nonbnc
    nonbnc+=binomial(i+9,i)
    nonbnc-=8
print("Non bouncys:",nonbnc)

print(binomial(110,10) + binomial(109,9) - 10*100 - 2)
