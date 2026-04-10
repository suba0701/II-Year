from itertools import product

colors = ['red', 'green', 'blue']
result = product(colors, repeat=2)

for i in result:
    print(i)
