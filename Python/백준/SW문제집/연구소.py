from copy import deepcopy
from itertools import combinations as C
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
candis = []
answer = []
max_value = 0


def getZeros():
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0:
                candis.append((row, col))


def dfs(tmp_board, x, y, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    tmp_board[x][y] = 2
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and tmp_board[nx][ny] == 0:
            dfs(tmp_board, nx, ny, n, m)


getZeros()
combis = list(C(candis, 3))
for combi in combis:
    tmp_board = deepcopy(board)
    for x, y in combi:  # 벽
        tmp_board[x][y] = 1
    #
    for row in range(n):
        for col in range(m):
            if tmp_board[row][col] == 2:
                dfs(tmp_board, row, col, n, m)
    safe = 0
    for row in tmp_board:
        safe += row.count(0)
    if max_value < safe:
        max_value = safe

print(max_value)
