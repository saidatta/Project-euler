diagonal = 1
start = 1
for width in range(3, 1002, 2):
    increment = width - 1
    count = increment * 4
    diagonal = diagonal + start * 4 + increment * 10
    start += count

print(diagonal)
