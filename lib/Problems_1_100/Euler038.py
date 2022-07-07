LIMIT = (10 ** 9) // 2


def compute():
    ans = ""
    # These numbers are here. because 2 and 3 digit numbers with product will result in a non-9 digit result.
    LOWER = 9123
    UPPER = 9876
    for n in range(2, 10):
        for i in range(LOWER, UPPER):
            s = "".join(str(i * j) for j in range(1, n + 1))
            if "".join(sorted(s)) == "123456789":
                ans = max(s, ans)
    return ans


if __name__ == "__main__":
    print(compute())

