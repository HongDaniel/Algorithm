rows = 3
columns = 3


def zeroCounter(board):
    cnt = 0
    for row in board:
        cnt += row.count(0)
    return cnt


def exit2(i):
    board = [[0]*columns for i in range(rows)]
    num = 1
    board[0][0] = 1
    x, y = 0, 0
    while(i):
        if num % 2 == 0:  # 짝수
            num += 1
            x += 1
            if x == rows:
                x = 0
            board[x][y] = num
        else:  # 홀수
            num += 1
            y += 1
            if y == columns:
                y = 0
            board[x][y] = num
        i -= 1
    return board


def solution(rows, columns):
    answer = []
    board = [[0]*columns for i in range(rows)]
    num = 1
    board[0][0] = 1
    x, y = 0, 0
    zeros = []
    while(1):
        if num % 2 == 0:  # 짝수
            num += 1
            x += 1
            if x == rows:
                x = 0
            board[x][y] = num
        else:  # 홀수
            num += 1
            y += 1
            if y == columns:
                y = 0
            board[x][y] = num
        print(board)

        zeros.append(zeroCounter(board))
        print(zeros)
        if zeroCounter(board) == 0:  # 탈출조건 1
            break
        if len(zeros) > 3 and zeros[-1] == zeros[-2] == zeros[-3]:  # 탈출조건 2
            return exit2(len(zeros)-2)

    print(f"final board:{board}")
    return answer


solution(rows, columns)
