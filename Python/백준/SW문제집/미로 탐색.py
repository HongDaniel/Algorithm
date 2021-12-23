from collections import deque
n, m = map(int, input().split())
board = []
dx = [0, 0, 1, -1]  # 방향
dy = [1, -1, 0, 0]
check = [[False]*m for i in range(n)]
dist = [[0]*m for i in range(n)]
q = deque()

# 정보입력
for row in range(n):
    board.append(list(map(int, input())))

q.append((0, 0))  # 시작점
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == False and board[nx][ny] == 1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
                check[nx][ny] = True

print(board)
print(dist)
print(dist[n-1][m-1] + 1)
