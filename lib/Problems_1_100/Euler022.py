
import requests

r = requests.get('https://projecteuler.net/project/resources/p022_names.txt')

def worth(name): return sum(ord(letter) - ord('A') + 1 for letter in name)

names = r.text.replace('"', '').split(',')
names.sort()

print(sum((i + 1) * worth(names[i]) for i in range(0, len(names))))
