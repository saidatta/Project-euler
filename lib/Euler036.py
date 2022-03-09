# print(sum(n for n in range(1, 1000000)
#           if str(n)[::-1] == str(n) and bin(n)[2:] == bin(n)[-1:1:-1]))

from Euler import is_palindromic
print(sum(n for n in range(1, 1000000) if is_palindromic(str(n)) and is_palindromic(bin(n)[2:])))
