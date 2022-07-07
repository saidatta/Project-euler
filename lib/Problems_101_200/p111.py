from lib.Eulerlib import is_prime

'''
The generator function creates the duplicates i.e. for n=4, '100'+'9' is the same as '1'+'009'. Rather than add code 
to avoid this, it was simpler to add the results to a set.

Runs in approx 1 sec.
'''
def insert_digit(seed, numDigits):
    for i in range(0, len(seed) + 1):
        for digit in range(0, 10):
            temp = seed[:i] + str(digit) + seed[i:]
            if numDigits == 1:
                yield temp
            else:
                yield from insert_digit(temp, numDigits - 1)


n = 10
answer = set()
for d in range(0, 10):
    found = False
    for numOfDigitsToAdd in range(1, n):
        seed = (n - numOfDigitsToAdd) * str(d)
        for i in insert_digit(seed, numOfDigitsToAdd):
            if is_prime(int(i)) and i[0] != '0':
                answer.add(int(i))
                found = True
        if found: break

print(sum(answer))
