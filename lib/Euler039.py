def compute():
    ans = max(range(1, 1001), key=count_solutions)
    return str(ans)

# We are given two equations to work with
# a2 + b2 = c2 (1)
# a + b+ c = p (2)
# Thus we can rewrite (2) as c = p  – a – b and insert it into (1) yielding
# a2 + b2 = (p-a-b)2 = p2 + a2 + b2 -2pa – 2pb + 2ab
# Isolating b on one side of that equation yields
# b = (p2 -2pa) / (2p-2a)

# if a and b is even so is c and thus p is even
# if a or b (but not both) is odd then c is odd and thus p is even
# if both a and b is odd then c is even and thus p is even
# Therefore we only need to check the numbers where p is even.
def count_solutions(p):
    result = 0
    for a in range(1, (p // 3)):
            if (p**2 - 2 * p * a) % (2 * (p - a)) == 0:
                result += 1
    return result


if __name__ == "__main__":
    print(compute())