
def can_construct(n, target_sum, target_prod, max_val):
    if max_val == 1:
        return target_prod == 1 and target_sum == n
    if target_prod == 1:
        return target_sum == n
    mv = target_sum - n + 1
    for v in range(min(mv, max_val), 0, -1):
        if target_prod % v == 0 and can_construct(n - 1, target_sum - v, target_prod // v, v):
            return True

def find_min_product_sum(n):
    target = n
    while not can_construct(n, target, target, target):
        target += 1
    return target

results = set()
for n in range(2, 12001):
    result = find_min_product_sum(n)
    results.add(result)

print("Sum =", sum(results))