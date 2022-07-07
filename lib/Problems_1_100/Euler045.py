from lib.Numbers import isPentagonalNumber

result, i = 0, 143

while True:
    i += 1
    result = i * ( 2 * i - 1)

    if (isPentagonalNumber(result)):
        break
print(result)
