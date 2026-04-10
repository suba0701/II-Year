from collections import deque

nums = [1, 2, 3, 4, 5, 6]
k = 3

window = deque(nums[:k])
curr_sum = sum(window)

print(curr_sum)  # 6


for n in nums[k:]:
    curr_sum = curr_sum - window.popleft() + n
    window.append(n)
    print(curr_sum)
