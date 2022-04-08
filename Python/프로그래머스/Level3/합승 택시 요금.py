import heapq
from math import inf
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


def dijkstra(start, dst):
    global graph
    n = len(graph)
    table = [inf for i in range(n)]
    table[start] = 0  # 자기 자신으로 가는 거리는 0
    q = []
    heapq.heappush(q, [0, start])
    while(q):
        cost, node = heapq.heappop(q)
        if cost > table[node]:
            continue
        for item in graph[node]:
            connected_node, ncost = item
            ncost += cost
            if ncost < table[connected_node]:
                table[connected_node] = ncost
                heapq.heappush(q, [ncost, connected_node])
    return table[dst]


def solution(n, s, a, b, fares):
    global graph
    answer = inf
    graph = [[] for i in range(n+1)]
    for fare in fares:
        i, j, cost = fare
        graph[i].append([j, cost])
        graph[j].append([i, cost])

    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    print(answer)
    return answer


solution(n, s, a, b, fares)
