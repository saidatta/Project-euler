num, den, count = 3, 2, 0
for iter_x in range(0, 1000):
    num, den = num + den + den, num + den
    if len(str(num)) > len(str(den)):
        count += 1
print(count)
