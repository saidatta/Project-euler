# https://projecteuler.net/project/resources/p042_words.txt

import itertools
import requests

def compute():
    ans = sum(1
              for s in WORDS
              if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
    return str(ans)


def is_triangular_number(n):
    temp = 0
    for i in itertools.count():
        temp += i
        if n == temp:
            return True
        elif n < temp:
            return False


WORDS = requests.get("https://projecteuler.net/project/resources/p042_words.txt").text.replace('"', '').split(',')


if __name__ == "__main__":
    print(compute())
