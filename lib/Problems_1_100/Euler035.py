from lib import euler


def compute():
    isprime = Euler.list_primality(999999)
    def is_circular_prime(n):
        s = str(n)
        allTrue = all(isprime[int(s[i : ] + s[ : i])]  for i in range(len(s)))
        return allTrue

    ans = sum(1
              for i in range(len(isprime))
              if is_circular_prime(i))
    return str(ans)


if __name__ == "__main__":
    print(compute())
