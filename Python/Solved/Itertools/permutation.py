from itertools import permutations

s = '123'
result = permutations(s)

for i in result:
    print(''.join(i))
