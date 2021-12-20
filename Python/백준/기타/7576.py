from collections import deque

col, row = map(int, input().split())
graph = [list(map(int, input().split()))for i in range(row)]  # 띄어
visited = [[0]*col for i in range(row)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            if 0 <= newx < row and 0 <= newy < col:
                if graph[newx][newy] == 0:
                    graph[newx][newy] = graph[x][y]+1
                    q.append([newx, newy])


# main()
q = deque()
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()
answer = 0
for row in graph:
    if 0 in row:
        answer = -1
        break
    if answer < max(row):
        answer = max(row)

# print(graph)
if answer == -1:
    print(answer)
else:
    print(answer-1)
