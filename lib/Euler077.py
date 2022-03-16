# int target = 2;
# int[] primes = ESieve(2, 1000);
#
# while (true) {
# int[] ways = new int[target+1];
# ways[0] = 1;
#
# for (int i = 0; i < primes.Length; i++) {
# for (int j = primes[i]; j <= target; j++) {
# ways[j] += ways[j - primes[i]];
# }
# }
#
# if (ways[target] > 5000) break;
# target++;
# }
from Euler import prime_sieve
target = 2
primes = prime_sieve(1000)
# while (True):
#     ways = [1] + [0] * (target + 1)
#     for i in range(0, len(primes)):
#         for j in range(primes[i], target + 1):
#             ways[j] += ways[j - primes[i]]


# target = 100

while True:
    nums = [1] + [0] * target
    for x in range(0, len(primes)):
        #if I have to give change to n pennies,
        # if I give back one coin of x how many ways can I give back the rest n-x pennies using
        # only coins of value x or smaller.
        for i in range(primes[x], target + 1):
            nums[i] += nums[i - primes[x]]

    if (nums[target] > 5000):
        break
    target += 1

print(target)
