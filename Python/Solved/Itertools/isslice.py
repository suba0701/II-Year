from itertools import cycle, islice

letters = ['a', 'b']
result = islice(cycle(letters), 6)

for i in result:
    print(i)
