
dig_sum_max = 0
for a in range(0, 100):
    for b in range(0, 100):
        digital_sum = sum(int(digit) for digit in str(a ** b))
        if digital_sum > dig_sum_max: dig_sum_max = digital_sum
print(dig_sum_max)
