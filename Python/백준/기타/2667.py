from sys import stdin
n = int(input())
graph = [[0]*n for i in range(n)]
visited = [[0]*n for i in range(n)]
answer = []
print(graph)
print(visited)

dx = [1, -1, 0, 0]  # 동서남북
dy = [0, 0, -1, 1]

for i in range(len(graph)):  # 그래프 입력받기
    line = stdin.readline().strip()
    for j, number in enumerate(line):
        graph[i][j] = int(number)


def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    for i in range(4):
        newx = x+dx[i]
        newy = y+dy[i]
        if newx >= 0 and newx < n and newy >= 0 and newy < n:
            if visited[newx][newy] == 0 and graph[newx][newy] == 1:
                dfs(newx, newy)


# main()
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            houses.append(cnt)
houses.sort()
print(len(houses))
for house in houses:
    print(house)
