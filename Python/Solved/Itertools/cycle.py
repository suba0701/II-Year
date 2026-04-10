from itertools import cycle

numbers = [5, 10, 15]
c = cycle(numbers)

for i in range(3):
    print(next(c))
