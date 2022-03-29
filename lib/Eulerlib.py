import array, math


# Returns the number of 1's in the binary representation of
# the non-negative integer x. Also known as Hamming weight.
def popcount(x):
	return bin(x).count("1")


# Given integer x, this returns the integer floor(sqrt(x)).
def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y


# Tests whether the given integer is a prime number.
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True

# Yields prime numbers in ascending order from 2 to limit (inclusive).
def prime_generator(limit):
	if limit >= 2:
		yield 2
	
	# Sieve of Eratosthenes, storing only odd numbers starting at 3
	isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
	sieveend = sqrt(limit)
	for i in range(len(isprime)):
		if isprime[i] == 1:
			p = i * 2 + 3
			yield p
			if i <= sieveend:
				for j in range((p * p - 3) >> 1, len(isprime), p):
					isprime[j] = 0


def list_smallest_prime_factors(n):
	result = [None] * (n + 1)
	limit = sqrt(n)
	for i in range(2, len(result)):
		if result[i] is None:
			result[i] = i
			if i <= limit:
				for j in range(i * i, n + 1, i):
					if result[j] is None:
						result[j] = i
	return result


def list_totients(n):
	result = list(range(n + 1))
	for i in range(2, len(result)):
		if result[i] == i:  # i is prime
			for j in range(i, len(result), i):
				result[j] -= result[j] // i
	return result

# Returns x^-1 mod m. Note that x * x^-1 mod m = x^-1 * x mod m = 1.
def reciprocal_mod(x, m):
	assert 0 <= x < m
	
	# Based on a simplification of the extended Euclidean algorithm
	y = x
	x = m
	a = 0
	b = 1
	while y != 0:
		a, b = b, a - x // y * b
		x, y = y, x % y
	if x == 1:
		return a % m
	else:
		raise ValueError("Reciprocal does not exist")


def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


# Decorator. The underlying function must take only positional arguments, no keyword arguments.
class Memorize:
	
	def __init__(self, func):
		self.func = func
		self.cache = {}
	
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val
