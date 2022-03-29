import itertools


def compute():
    nums = set()
    for i in range(1, 10001):
        sigma = i * i
        for j in itertools.count(i + 1):
            sigma += j * j
            if sigma >= 10 ** 8:
                break
            s = str(sigma)
            if s == s[::-1]:  # Is palindrome
                nums.add(sigma)
    return str(sum(nums))


if __name__ == "__main__":
    print(compute())
