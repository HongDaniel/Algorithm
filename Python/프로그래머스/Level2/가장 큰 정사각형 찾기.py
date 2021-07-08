board = [[1, 0], [0, 0]]


def solution(board):
    answer = 0
    rows = len(board)
    cols = len(board[0])

    if rows < 2 or cols < 2:  # 행이나 열의 길이가 1일 경우
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    return 1
        return 0

    for row in range(1, rows):
        for col in range(1, cols):
            if board[row][col] == 1:
                if board[row-1][col] == 0 or board[row][col-1] == 0 or board[row-1][col-1] == 0:
                    pass
                else:
                    board[row][col] = min(
                        board[row-1][col], board[row][col-1], board[row-1][col-1])+1
                    if answer < board[row][col]:
                        answer = board[row][col]

    if answer == 0:  # 1첫째 행,열에 1이 존재할 경우
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    return 1
    answer *= answer
    print(answer)
    return answer


solution(board)
