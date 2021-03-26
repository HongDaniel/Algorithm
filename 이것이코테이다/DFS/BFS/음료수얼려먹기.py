from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]


# print(graph)


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)  # 남
        dfs(x, y+1)  # 동
        dfs(x-1, y)  # 북
        dfs(x, y-1)  # 서
        return 1
    else:
        return 0


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(f"answer : {answer}")
print(graph)
