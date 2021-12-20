from collections import deque
dx = [1, -1, 0, 0]  # 동 서 북 남
dy = [0, 0, 1, -1]


def bfs(board, row, col):
    visited = [[]for i in range(row)]  # 방문지점
    distance = [[]for i in range(row)]  # 거리
    waterq = []
    for r in range(row):  # 거리, 방문지점 초기화
        for c in range(col):
            distance[r].append(0)
            visited[r].append(0)
            if board[r][c] == 'D':
                start = [r, c]
            if board[r][c] == 'S':
                endx, endy = r, c
            if board[r][c] == '*':  # 물 시작시점
                waterq.append([r, c])

    # 물을 먼저 채우기
        tmpwater = list(waterq)
        while(1):  # 물을 채우는 과정
            if len(tmpwater) == 0:
                break
            wx, wy = tmpwater.pop(0)
            for i in range(4):
                nextwx = wx+dx[i]
                nextwy = wy+dy[i]
                if 0 <= nextwx < row and 0 <= nextwy < col and board[nextwx] and board[nextwx][nextwy] == '.' and board[nextwx][nextwy] == 'S':
                    # print([nextwx, nextwy])
                    board[nextwx][nextwy] = '*'
                    waterq.append([nextwx, nextwy])

    q = [start]
    flag = False
    while q:
        x, y = q.pop(0)
        # print((x, y))
        visited[x][y] = 1
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            if 0 <= newx < row and 0 <= newy < col:
                if visited[newx][newy] == 0 and board[newx][newy] != '*' and board[newx][newy] != 'X':
                    q.append([newx, newy])
                    distance[newx][newy] = distance[x][y]+1
        # print(distance)
                if [newx, newy] == [endx, endy]:
                    flag = True
        if flag:
            break

    if distance[endx][endy]:
        return distance[endx][endy]
    else:
        return 'KAKTUS'


def solution():
    # row, col = map(int, input().split())
    # board = [list(map(str, input())) for _ in range(row)]
    row, col = 3, 3
    board = [['D', '.', '*'], ['.', '.', '.'], ['.', '.', 'S']]
    answer = bfs(board, row, col)
    print(answer)
    # print(board)


solution()
