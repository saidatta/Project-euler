import requests

r = requests.get('https://projecteuler.net/project/resources/p067_triangle.txt')
downloaded_triangle = []
for line in r.iter_lines():
    line = line.decode('utf-8')
    current = line.split(" ")
    # converting a string of array to int array.
    downloaded_triangle.append(list(map(int, current)))


for x in range(len(downloaded_triangle) - 1, -1, -1):
    for y in range(0, x):
        downloaded_triangle[x - 1][y] += max(downloaded_triangle[x][y], downloaded_triangle[x][y + 1])

print(downloaded_triangle[0][0])
