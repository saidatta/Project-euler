#Project Euler Problem 94
# Didnt submit because I didnt understand the solution

x, y, limit, result = 2, 1, 10 ** 9, 0

while True:
    # b = a + 1
    aTimes3 = 2 * x - 1
    areaTimes3 = y * (x - 2)
    if (aTimes3 > limit):
        break

    if (aTimes3 > 0 and areaTimes3 > 0 and aTimes3 % 3 == 0 and areaTimes3 % 3 == 0) :
        a = aTimes3 // 3
        area = areaTimes3 // 3

        result += 3 * a + 1

    # b = a + 1
    aTimes3 = 2 * x + 1
    areaTimes3 = y * (x + 2)
    if aTimes3 > limit:
        break

    if (aTimes3 > 0 and areaTimes3 > 0 and aTimes3 % 3 == 0 and areaTimes3 % 3 == 0) :
        a = aTimes3 // 3
        area = areaTimes3 // 3

        result += 3 * a - 1

    nextX = 2 * x + y * 3
    nextY = y * 2 + x
    x, y = nextX, nextY

print(result)