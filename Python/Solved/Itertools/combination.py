from itertools import combinations

items = ['A', 'B', 'C', 'D']
result = combinations(items, 2)

for i in result:
    print(i)
