from lib.Euler import is_pandigital

fn2, fn1, fn = 1, 1, 0

tailcut = 10 ** 9
n, found = 2, False

while not found:
    n += 1
    fn = (fn1 + fn2) % tailcut
    fn2 = fn1
    fn1 = fn

    if(is_pandigital(fn)):
        t = (n * 0.20898764024997873 - 0.3494850021680094)
        if is_pandigital(pow(10,t - int(t) + 8)):
            found = True

print(n)
print(fn)