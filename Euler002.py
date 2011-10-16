x,y , a =  1, 1, 0 
while (y < 4000000): 
  a += (x + y)
  (x, y) = [ x + 2*y, 2*x + 3*y ]
print a
