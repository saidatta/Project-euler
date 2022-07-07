target = 100
nums = [1] + [0] * target

for x in range(1, target):
    #f I have to give change to n pennies,
    # if I give back one coin of x how many ways can I give back the rest n-x pennies using
    # only coins of value x or smaller.
    for i in range(x, target + 1):
        nums[i] += nums[i - x]

print(nums[target])
