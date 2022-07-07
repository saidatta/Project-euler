
LIMIT = 1001
diag_sum = 1
diag_sum += sum(4 * width * width - 6 * (width - 1) for width in range(3, LIMIT+1, 2))

print(diag_sum)