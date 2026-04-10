from collections import deque

def is_palindrome(s: str) -> bool:
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("level"))   
print(is_palindrome("python"))  # Not palindrome -> False
