import heapq

a = []
heapq.heapify(a)
a.append(1)
a.append(5)
a.append(2)
a[0] = 9
print(a)
# print(a.pop())
# print(a.pop())
# print(a.pop())
