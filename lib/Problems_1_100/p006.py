import math

i = 0
sum = 0
while i < 101:
    sum += math.pow(i, 2)
    i += 1

y = math.pow(5050, 2) - sum
print("%d" % y)
