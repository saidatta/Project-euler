import math

def isPentagonalNumber(number):
    # n(3n -1)/2 = Pn; if you have pentagonal number,
    # Then you can inverse that function as below and check if its an integer.
    penTest = (math.sqrt(1 + 24 * number) + 1) / 6
    return penTest == int(penTest)