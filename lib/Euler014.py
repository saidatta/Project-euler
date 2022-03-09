# from numpy import *
from array import array

limit = 1_000_000

# a = array( [-1]*10)
# print (a)
sequence_len, starting_number = 0, 0
cache = [-1] * limit
cache[1] = 1

# Since I start from the smallest number, I know that every time my
# sequence of numbers decreases below the starting number,
# I have already calculated the remaining starting length.
# So for even numbers that happens after the first iteration.
for i in range(2, limit):
    sequence = i
    k = 0
    while (sequence != 1 and sequence >= i):
        k += 1
        if ((sequence % 2) == 0):
            sequence //= 2
        else:
            sequence = sequence * 3 + 1
    cache[i] = k + cache[sequence]
    if cache[i] > sequence_len:
        sequence_len = cache[i]
        starting_number = i

print (starting_number)
# for i in range(1, limit):
#     temp = i
#     count = 0
#
#     while temp != 1:
#         if temp % 2 == 0:
#             temp /= 2
#             count += 1
#         else:
#             temp = (3 * temp) + 1
#             count += 1
#
#     if count > longest_count:
#         longest_collatz = i
#         longest_count = count
#
# print(longest_collatz)