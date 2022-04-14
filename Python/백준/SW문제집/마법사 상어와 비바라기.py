n, m = map(int, input().split())
board = [[]for i in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))
moves = []
for i in range(m):
    x, y = map(int, input().split())
    moves.append((x, y))
dx = [0, -1, -1, -1, 0, 1, 1, 1]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]


def step1(clouds, move):
    di, si = move
    movex, movey = dx[di-1], dy[di-1]
    nclouds = []
    for cloud in clouds:
        x, y = cloud
        for i in range(si):
            x += movex
            y += movey
            if x < 0:
                x = n-1
            if x > n-1:
                x = 0
            if y < 0:
                y = n-1
            if y > n-1:
                y = 0
        nclouds.append([x, y])
    return nclouds


def step2(board, clouds):  # 각 칸에 비가 내린다
    for cloud in clouds:
        x, y = cloud
        board[x][y] += 1
    return board


def step3(board, rained):  # 대각선 체크
    diagnal = [1, 3, 5, 7]
    for r in rained:
        x, y = r
        cnt = 0
        for i in diagnal:
            movex, movey = dx[i], dy[i]
            nx = x+movex
            ny = y+movey
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt
    return board


def step4(board, visited):
    nclouds = []
    for row in range(n):
        for col in range(n):
            if board[row][col] >= 2 and visited[row][col] == 0:
                board[row][col] -= 2
                nclouds.append([row, col])
    return board, nclouds


for move in moves:
    clouds = step1(clouds, move)  # 구름을 이동시킨다.
    board = step2(board, clouds)  # 비가 내린다.
    rained = list(clouds)
    board = step3(board, rained)
    visited = [[0]*n for i in range(n)]
    for x, y in rained:
        visited[x][y] = 1
    board, clouds = step4(board, visited)
    # print(board)
    # print()
answer = 0
for row in board:
    answer += sum(row)
print(answer)
