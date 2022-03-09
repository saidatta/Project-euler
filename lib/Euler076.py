temp = 100
nums = [1]+[0]*temp

for x in range(1,temp):
  for i in range(x, temp+1):
    nums[i] += nums[i-x]
 
print nums[temp]

