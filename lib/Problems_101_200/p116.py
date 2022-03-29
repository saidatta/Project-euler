def compute():
    LENGTH = 5
    return str(sum(count_ways(LENGTH, i) for i in range(2, 5)))

def count_ways(length, m):
    ways = [1] + [0] * length
    for n in range(1, len(ways)):
        ways[n] += ways[n - 1]

        x = n
        while x > 0:
            ways[n] += ways[n - m]
            x -= m
        # for x in range(m, n)
        # if n >= m:
        #     ways[n] += ways[n - m]

    return ways[-1] - 1


if __name__ == '__main__':
    print(compute())