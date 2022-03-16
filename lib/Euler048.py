total_sum = 0
mod = pow(10, 10)
for x in range(1, 1001):
    total_sum = total_sum + pow(x, x)

print(total_sum % mod)
