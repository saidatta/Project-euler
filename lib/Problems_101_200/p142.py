import itertools
from collections import defaultdict

'''
First, find pairs of (pairs of squares) whose midpoints are equal. Then, calculate x, y, z and check if y + z and y - z
are squares. The checks for the other values (x + y, x - y, ...) have already been done by construction. 
I kept increasing the search space manually until it popped out an answer. 
'''
def main():
    def isrt(n):
        r = round(n**0.5)
        return r * r == n

    sq = {i:(i*i) for i in range(1, 1000)}
    z = defaultdict(list)
    for i, a in sq.items():
        for j, b in sq.items():
            if i < j and (a + b) % 2 == 0:
                z[(a + b) // 2].append((i, j))

    for pt, vec in z.items():
        done = False
        for u, v in itertools.combinations(vec, 2):
            x = (u[0]**2 + u[1]**2) // 2
            y = max(u[1], v[1])**2 - x
            z = min(u[1], v[1])**2 - x
            if isrt(y + z) and isrt(y - z):
                print("FOUND ANSWER", x, y, z, x + y + z)
                done = True
                break
        if done:
            break

if __name__ == "__main__":
    main()