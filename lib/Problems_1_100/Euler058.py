import fractions, itertools
from lib import euler

# From the diagram, let's observe the four corners of an n * n square (where n is odd).
# It's not hard to convince yourself that:
# - The bottom right corner always has the value n^2.
# Working clockwise (backwards):
# - The bottom left corner has the value n^2 - (n - 1).
# - The top left corner has the value n^2 - 2(n - 1).
# - The top right has the value n^2 - 3(n - 1).
# Furthermore, the number of elements on the diagonal is 2n - 1.


def compute():
    TARGET = fractions.Fraction(1, 10)
    numPrimes = 0
    for n in itertools.count(1, 2):
        for i in range(4):
            if Euler.is_prime(n * n - i * (n - 1)):
                numPrimes += 1
        # total # of nums in spiral is 2*n-1, where n is the side length.
        if n > 1 and fractions.Fraction(numPrimes, n * 2 - 1) < TARGET:
            return str(n)


if __name__ == "__main__":
    print(compute())