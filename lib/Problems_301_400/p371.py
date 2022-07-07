with500, no500 = 2, 0
for i in range(499, -1, -1):
    no500 = (with500 + (998 - 2 * i) * no500 + 1000) / (999 - i)
    with500 = (1000 + (1000 - 2 * i) * with500) / (1000 - i)
print('{0:.8f}'.format(no500))