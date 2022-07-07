import math

result, pmax = 0, 0

for D in range(2, 1001):
    limit = int(math.sqrt(D))
    if (limit ** 2 == D):
        continue
    m, d, a = 0, 1, limit
    numm1, num = 1, a
    denm1, den = 0, 1

    # pells equation
    while num ** 2 - D * (den **2) != 1:
        m = d * a - m
        d = (D - m ** 2) // d
        a = (limit + m) // d

        numm2 = numm1
        numm1 = num
        denm2 = denm1
        denm1 = den

        num = a * numm1 + numm2
        den = a * denm1 + denm2

    if (num > pmax):
        pmax = num
        result = D


print(result)