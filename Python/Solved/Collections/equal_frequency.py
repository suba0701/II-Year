from collections import Counter

s = "aabbccddeegg"

def all_equal_frequency(s: str) -> bool:
    if not s:
        return True  # decide: empty string treated as "all equal"
    counts = Counter(s)
    return len(set(counts.values())) == 1

print(all_equal_frequency(s))  # True
