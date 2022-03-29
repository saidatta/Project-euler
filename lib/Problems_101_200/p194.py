import time
import sys
import itertools
import operator
import functools

# With two fixed points on the left, I compute the number of possible graphs A with respectively  colors (a_base_case).
# I do the same for the B graphs (b_base_case). Then for a given number of colors c I can compute the number of
# legit A graphs (number_ways_a) : (1 among c-2)*a_base_case[0]+...+(5 among c-2)*a_base_case[5].
# I do the same for B graphs.
#
# Finally I need to fix the first two point of the succesions of A and B graphs : c * (c-1), then I take into account
# the position of the A graphs among the A and B graphs : a amon a+b.

class Problem():

    def __init__(self):
        self.res = 0
        self.a = 25
        self.b = 75
        self.c = 1984
        self.a_base_case = []
        self.b_base_case = []

    def init_base_cases(self):
        for i in range(3, 8):
            digits = list(range(1, i+1))
            set_digits = set(digits)
            l = [digits] * 7
            count_a = 0
            count_b = 0
            for k in itertools.product(*l):
                if k[5]==1 and k[6]==2 and set(k)==set(set_digits):
                    if k[0]!=1 and k[0]!=k[3] and k[0]!=k[1] and k[1]!=k[2] and k[2]!=2 and k[2]!=k[4] and k[3]!=1 and k[3]!=k[4]:
                        count_b += 1
                        if k[4]!=2:
                            count_a += 1
            self.a_base_case.append(count_a)
            self.b_base_case.append(count_b)

    @staticmethod
    def choose(n, r):
        r = min(r, n - r)
        numer = functools.reduce(operator.mul, range(n, n - r, -1), 1)
        denom = functools.reduce(operator.mul, range(1, r + 1), 1)
        return numer // denom

    def get_res(self):
        choose_list = [self.choose(self.c - 2, i) for i in range(1, 6)]
        lists_a = self.a_base_case, choose_list
        number_ways_a = sum([x * y for x, y in zip(*lists_a)])
        lists_b = self.b_base_case, choose_list
        number_ways_b = sum([x * y for x, y in zip(*lists_b)])
        self.res = (self.c*(self.c-1)*number_ways_a**self.a*number_ways_b**self.b*self.choose(self.a+self.b, self.a))%10**8

    def solve(self):
        self.init_base_cases()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('execution ', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    main()
    sys.exit()
