from collections import deque

col, row, height = map(int, input().split())
graph = [[list(map(int, input().split()))for i in range(row)]
         for i in range(height)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while len(q) != 0:
        h, x, y = q.popleft()
        for i in range(6):
            newx = x+dx[i]
            newy = y+dy[i]
            newh = h+dz[i]
            if 0 <= newx < row and 0 <= newy < col and 0 <= newh < height:
                if graph[newh][newx][newy] == 0:
                    graph[newh][newx][newy] = graph[h][x][y]+1
                    q.append([newh, newx, newy])


# main()
q = deque()
for h in range(height):
    for i in range(row):
        for j in range(col):
            if graph[h][i][j] == 1:
                q.append([h, i, j])

bfs()
# print(graph)
answer = 0
# 가장 오래 익는데 걸리는 토마토 구하기
flag = True
for h in range(height):
    for x in range(row):
        for y in range(col):
            if graph[h][x][y] == 0:
                flag = False
            answer = max(answer, graph[h][x][y])

if flag:
    print(answer-1)
else:
    print(-1)
