from collections import Counter

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 3, 4, 4, 5]

extra = Counter(list2) - Counter(list1)
print(extra)         
print(list(extra.elements()))  
