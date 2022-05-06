import heapq
from collections import defaultdict
n, m = map(int, input().split())
road = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)
x, k = map(int, input().split())

time = 0


def dij(start, end):
    minDis = [987654321]*(n+1)  # 최단거리
    visited = [False]*(n+1)  # 방문여부
    minDis[start] = 0
    t = 3
    while(1):
        if visited.count(True) == n:
            break
        visited[start] = True
        for el in road[start]:
            if minDis[el] > minDis[start]+1:
                minDis[el] = minDis[start]+1
        tmpMinDis = 987654321
        minIdx = -1
        for i in range(n+1):
            if visited[i] == False:
                flag = True
                if minDis[i] < tmpMinDis:
                    tmpMinDis = minDis[i]
                    minIdx = i
        start = minIdx
        if minIdx == -1:
            return -1
        t -= 1
    return minDis[end]


a = dij(1, k)
b = dij(k, x)
if a == -1 or b == -1:
    print(-1)
else:
    print(a+b)
