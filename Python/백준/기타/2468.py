n = int(input())
board = [[] for i in range(n)]
for r in range(n):
    board[r] = (list(map(int, input().split(" "))))


max_height = 0
for r in board:
    if max_height < max(r):
        max_height = max(r)
candis = []


def fill_water(board, water):
    tmp = list(board)
    for row in range(n):  # 침수과정
        for col in range(n):
            if tmp[row][col] < water+1:
                tmp[row][col] = -1
    cnt = 0
    return (tmp)


def seperate(board, water):
    newboard = fill_water(board, water)
    visited = []
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    for row in range(n):  # 영역탐방
        for col in range(n):
            if newboard[row][col] > 0 and (row, col) not in visited:
                # print(visited)
                q.append((row, col))
                while(q):
                    cx, cy = q.pop(0)
                    visited.append((cx, cy))
                    for i in range(4):
                        nx = cx+dx[i]
                        ny = cy+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and newboard[nx][ny] > 0:
                            q.append((nx, ny))
                # print(visited)
                cnt += 1

    # print(cnt)
    return cnt


# for water in range(4, len(max_height+1)):
for water in range(max_height+1):
    candis.append(seperate(board, water))
# print(candis)
print(max(candis))
