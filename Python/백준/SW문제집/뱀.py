from collections import deque
N = int(input())  # 보드의 크기
board = [[0]*N for i in range(N)]
K = int(input())  # 사과의 개수
for i in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())
turns = {}
for j in range(L):
    X, C = input().split()
    turns[int(X)] = C

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동 남 서 북
d_index = 0  # 처음에는 동쪽
x, y = 0, 0
board[0][0] = 2  # 출발위치
time = 1
visited = deque([[0, 0]])

while(1):
    # 해당방향으로 전진
    x = x+direction[d_index][0]
    y = y+direction[d_index][1]
    if 0 <= x < N and 0 <= y < N and board[x][y] != 2:
        if board[x][y] != 1:  # 사과가 없을 경우
            tmpx, tmpy = visited.popleft()
            board[tmpx][tmpy] = 0
        board[x][y] = 2
        visited.append([x, y])

        if time in turns.keys():
            if turns[time] == 'D':
                d_index = (d_index+1) % 4
            else:
                d_index = (d_index-1) % 4
        time += 1
    else:  # 벽에 부딪히거나 본인의 몸에 부딪힐 때
        break
print(time)
