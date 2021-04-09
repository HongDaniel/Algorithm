board = [[0, 0, 0, 0]]

rows = len(board)
cols = len(board[0])

if rows < 2 or cols < 2:
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                print(1)
    print(0)
