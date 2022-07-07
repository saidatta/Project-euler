import time


def is_bouncy(n: int) -> bool:
    l = list(str(n))
    s = sorted(l)
    return s != l and s != l[::-1]


def pe_p112() -> int:
    r, i = 1, 100
    while r / i < 0.99:
        if is_bouncy(i):
            r += 1
        i += 1
    return i


st = time.time()
print(pe_p112())
print(f"{time.time() - st} sec")