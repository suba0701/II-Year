from collections import defaultdict

words = ["python", "java", "go", "c", "ruby", "php"]

groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)

for length in sorted(groups):
    print(f"{length} → {groups[length]}")
