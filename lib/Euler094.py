#Project Euler Problem 94
# Didnt submit because I didnt understand the solution

side0, side, allPerimeterSum, perimeter, m = 1, 1, 0, 0, 1

L = 10**9
while perimeter <= L:
    side0, side, m = side, 4*side - side0 + 2*m, -m
    allPerimeterSum += perimeter
    perimeter = 3 * side - m

print("Sum of perimeters less than", L, " =", allPerimeterSum)
