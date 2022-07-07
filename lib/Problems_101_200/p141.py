import math

def pgcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
li=[]
for a in range(2,10000):
    for b in range(1,a):
        if pgcd(a,b)==1:
            k=1
            n=1
            while n<10**12:
                n=a*a*a*b*k*k+k*b*b
                r=math.sqrt(n)
                if math.floor(r)==r:
                    if n<10**12:
                        if n not in li:
                            li.append(n)
                k=k+1
print(sum(li))
