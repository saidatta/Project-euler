'''
This problem is directly from the concept of Diophantine Quadratic Equation and can be solved using a program. After i recevied 2 equation. Which are in the while loop for i and j. I DRastically reduced the computation by the method shown below.
'''


i = 85
j = 120
while j < 10**12:
  i,j = 3*i + 2*j - 2, 4*i + 3*j - 3 #the equation after the calculation.
  print i
