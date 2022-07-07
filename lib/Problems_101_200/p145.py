
c = 120  # reversible numbers below 1000
c += 20 * sum(30 ** i for i in range(1, 4))  # reversible numbers with an even number of digits
c += 50000  # reversible 7-digit numbers
print(c)