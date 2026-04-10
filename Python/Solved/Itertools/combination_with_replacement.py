from itertools import combinations_with_replacement

numbers = [1, 2]
result = combinations_with_replacement(numbers, 2)

for i in result:
    print(i)
