from itertools import combinations
from collections import Counter


temp = []
num = 2
orders = ["XYZ", "XWY", "WXA"]
for order in orders:
    for i in combinations(order, num):
        temp.append(i)

temp = Counter(temp)
most = temp.most_common()
modes = []
maximum = most[0][1]
for num in most:
    if num[1] == maximum:
        modes.append(''.join(num[0]))
print(modes)

# print(Counter(temp))
