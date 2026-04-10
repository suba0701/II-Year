from collections import defaultdict

data = [("Alice", 85), ("Bob", 78), ("Alice", 92), ("Bob", 88)]

marks = defaultdict(list)
for name, score in data:
    marks[name].append(score)

print(dict(marks))
