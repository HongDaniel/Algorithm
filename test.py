from collections import deque
a = deque([1, 2, 3, 2, 5, 2, 4])
tmp = a.remove(2)
a.append(2)
print(a)
