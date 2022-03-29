import requests

r = requests.get('https://projecteuler.net/project/resources/p089_roman.txt')

ROMAN_NUMERALS_PREFIXES = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

# e.g. (empty), I, II, III, IV, V, VI, VII, VIII, IX
DIGIT_LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]

TO_SIMPLIFY = []


def parse_roman_numeral(s):
    result = 0
    while len(s) > 0:
        for (prefix, val) in ROMAN_NUMERALS_PREFIXES:
            if s.startswith(prefix):
                result += val
                s = s[len(prefix):]
                break
        else:
            raise Exception("Cannot parse Roman numeral")
    return result


def roman_numeral_len(n):
    assert 1 < n < 5000
    result = 0
    if n >= 4000:  # 4000 is MMMM, which doesn't have a two-letter form
        result += 2  # Compensate for this fact
    while n > 0:
        result += DIGIT_LENGTHS[n % 10]
        n //= 10
    return result


def compute():
    for line in r.iter_lines():
        line = line.decode('utf-8')
        TO_SIMPLIFY.append(line)

    ans = sum(len(s) - roman_numeral_len(parse_roman_numeral(s)) for s in TO_SIMPLIFY)
    return str(ans)


if __name__ == "__main__":
    print(compute())
