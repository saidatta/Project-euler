from functools import reduce

LIMIT = 10 ** 6
def compute():
    s = "".join(str(i) for i in range(1, LIMIT))
    ans = (list(int(s[10**x - 1]) for x in range(1, 7)))
    return reduce((lambda x, y : x*y), ans)

if __name__ == "__main__":
    print(compute())