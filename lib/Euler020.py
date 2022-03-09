from Euler import factorial

factToString = str(factorial(100))
sumOfDigits = 0

print(factToString)

for x in range(0, len(factToString)):
    sumOfDigits += int(factToString[x])

print(sumOfDigits)