
# Generate all primes <= N (10^6 was large enough), then find all values of the form
# p^2q^3 <= N*N*8 (all squbes under that number are found), sort that, then brute force my way
# through checking for prime_proof_ness by trial division.

from lib.Euler import *


def squbes_please():
    N = 10**6
    primes = prime_sieve(N)
    combs = [comb for comb in permute_factors_in_powers(N*N*8, (2, 3), primes)]
    combs.sort()
    return(combs)

def is_prime_proof(n):
    number_list = list(digits(n))
    for digit in range(len(number_list)):
        for new_digit in range(10):
            new_num_list = number_list.copy()
            new_num_list[digit] = new_digit
            new_num = from_digits(new_num_list)
            if is_prime(new_num):
                return False
    return True

def main():
    i = 0
    for sqube in squbes_please():
        if "200" in str(sqube):
            if is_prime_proof(sqube):
                i += 1
                print(i, sqube)
            if i >= 200:
                break

if __name__ == "__main__":
    main()