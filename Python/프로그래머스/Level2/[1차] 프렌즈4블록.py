def pop_list(m, n, board):
    remove = [[0]*m for i in range(n)]
    for row in range(len(board)-1):
        for col in range(len(board[0])-1):
            if board[row][col] != -1 and board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                remove[row][col], remove[row+1][col], remove[row][col +
                                                                  1], remove[row+1][col+1] = 1, 1, 1, 1
    return remove


def pop(remove, board):
    cnt = 0
    copy_board = list(board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if remove[row][col] == 1:
                board[row].pop(col)
                board[row].insert(0, -1)
                cnt += 1
    return board, cnt


def solution(m, n, board):
    answer = 0
    trans_board = [[0]*m for i in range(n)]

    for row in range(m):
        for col in range(n):
            trans_board[col][row] = board[row][col]
    board = trans_board

    while(1):
        remove = pop_list(m, n, board)
        # print(f"board:{board} remove:{remove}")
        if sum(sum(el) for el in remove) == 0:
            break
        else:
            board, poped_num = pop(remove, board)
            answer += poped_num

    return answer
