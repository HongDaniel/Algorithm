from collections import deque
from itertools import combinations as C
from copy import deepcopy
n, m = map(int, input().split())
board = []
for row in range(n):
    board.append(list(map(int, input().split())))
chickens = []
distances = []


def get_chickendis(r, c, n, candi):
    distances = []
    for cx, cy in candi:
        distances.append(abs(r-cx)+abs(c-cy))
    return min(distances)


for r in range(n):  # 치킨집 추적
    for c in range(n):
        if board[r][c] == 2:
            chickens.append((r, c))

candis = list(C(chickens, m))  # 영업할 치킨집


for candi in candis:
    closed = deepcopy(chickens)
    new_board = deepcopy(board)
    for place in candi:
        closed.remove(place)
    for x, y in closed:  # 폐업
        new_board[x][y] = 0
        #
    distance = 0

    for r in range(n):
        for c in range(n):
            if new_board[r][c] == 1:
                distance += get_chickendis(r, c, n, candi)
                # print(get_chickendis(r, c, n, candi))
    distances.append(distance)

print(min(distances))
