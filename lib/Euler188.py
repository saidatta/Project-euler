t = 1  # temporary.
x, y, z = 1777, 1855, 8
while y:
    t = pow(x, t, 10 ** z)  # need the last 8 digits. hence 10**8
    y -= 1
print(t)
