def fact(n):
    f = 1
    for x in range(1, n+1): f = f * x
    return f

def permutation(orig_nums, n):
    nums = list(orig_nums)
    perm = []
    while len(nums):
        divider = fact(len(nums)-1)
        pos = n // divider
        n = n % divider
        perm.append(nums[pos])
        nums = nums[0:pos] + nums[pos+1:]
    return perm


print(''.join(str(x) for x in permutation(range(0, 10), 999999)))
