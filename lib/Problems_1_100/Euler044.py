from lib.Numbers import isPentagonalNumber

result, notFound, i = 0, True, 1

while notFound:
    i += 1
    # Pentagonal formula
    n = i * (3 * i - 1) // 2

    for j in range(i-1, 0, -1) :
        m = j * (3 * j - 1) // 2
        if (isPentagonalNumber(n - m) and isPentagonalNumber(n + m)):
            result = n-m
            notFound = False
            break

print(result)