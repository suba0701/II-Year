from datetime import datetime

t1 = datetime(2026, 3, 10, 10, 0, 0)
t2 = datetime(2026, 3, 10, 12, 30, 0)

delta = t2 - t1
print(int(delta.total_seconds()))  # 9000
