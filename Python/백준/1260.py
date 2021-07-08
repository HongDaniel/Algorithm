n, m, v = map(int, input().split())  # n- 정점의 개수 m- 간선의 개수 v- 시작점
# print(f"{n} {m} {v}")
visited = [False]*(n+1)  # 정점의 방문 여부
graph = [[0]*(n+1) for i in range(n+1)]  # 정점에 대한 그래프

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
# print(graph)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if(visited[i] == False and graph[v][i] == 1):
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = False
    while queue:
        left = queue.pop(0)
        print(left, end=' ')
        for i in range(1, n+1):
            if(visited[i] == True and graph[left][i] == 1):
                queue.append(i)
                visited[i] = False


dfs(v)
print()
bfs(v)
