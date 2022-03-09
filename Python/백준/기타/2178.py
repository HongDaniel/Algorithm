from collections import deque
n, m = map(int, input().split())
board = []
for row in range(n):
    board.append(list(map(int, input())))


def bfs(board, x, y, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([(x, y)])
    visited = [[0]*m for i in range(n)]
    while(q):
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
                board[nx][ny] = board[x][y]+1
                q.append((nx, ny))
    # print(visited)
    # for el in board:
    #     print(el)
    print(board[n-1][m-1])


bfs(board, 0, 0, n, m)
