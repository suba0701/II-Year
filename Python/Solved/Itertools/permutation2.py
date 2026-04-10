from itertools import permutations

items = ['X', 'Y', 'Z']
result = permutations(items)

for i in result:
    print(i)
