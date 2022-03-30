from copy import deepcopy
board = [[1, 1, 4, 3], [3, 2, 1, 4], [2, 1, 4, 2], [3, 1, 3, 3]]


def canBePoped(board, x, y, n):
    dx = [0, 0, 1, -1]  # 우 좌 하 상
    dy = [1, -1, 0, 0]
    horizon, vertical = 1, 1
    for i in range(2):  # 좌우
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == board[x][y]:  # 같을 경우
                horizon += 1
                while(1):
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == board[x][y]:
                        horizon += 1
                    else:
                        break

    for i in range(2, 4):  # 상하
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == board[x][y]:  # 같을 경우
                vertical += 1
                while(1):
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == board[x][y]:
                        vertical += 1
                    else:
                        break

    # print(f"horizon:{horizon}")
    # print(f"vertical:{vertical}")
    # for el in board:
    #     print(el)
    if vertical >= 3 or horizon >= 3:
        return True
    else:
        return False


def check(board, x, y, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    candis = []
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # print(f"dx[i]: {dx[i]} dy[i]:{dy[i]}")
        if 0 <= nx < n and 0 <= ny < n:
            new_board = deepcopy(board)
            # print(f"x:{x} y:{y} nx:{nx} ny:{ny}")
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            # for el in new_board:
            #     print(el)

            if canBePoped(new_board, x, y, n):
                candis.append(((x, y), (nx, ny)))
    if candis:
        return len(candis)
    else:
        return 0


def solution(board):
    answer = 0
    n = len(board)
    for row in range(n):
        for col in range(n):
            if check(board, row, col, n):  # 깨질 수 있나?
                answer += check(board, row, col, n)
    print(answer)
    if answer:
        return answer
    else:
        return -1


solution(board)
