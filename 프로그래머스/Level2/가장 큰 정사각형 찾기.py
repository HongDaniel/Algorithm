board = [[0, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [0, 0, 1, 0]]


def solution(board):
    row = len(board)
    col = len(board[0])

    ms = 1
    for r in range(row):
        temp = []
        print(f"r:{r+1}")
        for c in range(col):
            print(board[r][c])
            if(board[r][c] == 1):
                temp.append(c)
        ms = max(ms, min(len(temp), (r+1)))
        print(f"ms:{ms}")
    print(ms)
    return ms**2


solution(board)
