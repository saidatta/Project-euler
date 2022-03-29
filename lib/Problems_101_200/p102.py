import requests

triangles = requests.get("https://projecteuler.net/project/resources/p102_triangles.txt")


def compute():
    ans = 0
    for line in triangles.iter_lines():
        line = line.decode("utf-8")
        pts = list(map(int,line.split(",")))

        A, B, C = [pts[0], pts[1]], [pts[2], pts[3]], [pts[4], pts[5]]
        P = [0, 0]

        if (area(A, B, C) == area(A, B, P) + area(A, P, C) + area(P, B, C)):
            ans += 1
    return ans


def area(a, b, c):
    return abs((a[0] - c[0]) * (b[1] - a[1]) - (a[0] - b[0]) * (c[1] - a[1]))


if __name__ == "__main__":
    print(compute())
