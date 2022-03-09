from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
visited = [[0]*m for i in range(n)]


def turn_left(d):
    return (d-1) % 4


def dfs(board, visited, x, y, d, flag):
    # print((x, y))
    if flag:
        visited[x][y] = 2  # 현재위치 청소
    flag = False
    for i in range(4):
        d = turn_left(d)  # 왼쪽방향
        nx = x+direction[d][0]
        ny = y+direction[d][1]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and visited[nx][ny] == 0:
            flag = True
            dfs(board, visited, nx, ny, d, flag)
            break

    if flag == False:  # 청소할 곳이 없다면
        # 후진
        nx = x-direction[d][0]
        ny = y-direction[d][1]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
            dfs(board, visited, nx, ny, d, flag)
        else:
            return


dfs(board, visited, r, c, d, True)  # 1,1,0
total = 0
for el in visited:
    total += sum(el)//2
print(total)
