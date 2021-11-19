m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def reverse(board):
    newBoard = [[0]*len(board) for i in range(len(board[0]))]
    for row in range(len(board)):
        for col in range(len(board[row])):
            newBoard[col][row] = board[row][col]
    return newBoard


def isPop(board, row, col):
    if board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1] and board[row][col] != -1:
        return True
    else:
        return False


def pop(board, popList):
    poped = 0
    for candi in popList:  # pop
        row, col = candi[0], candi[1]
        board[row][col] = 0

    for row in board:
        while(1):
            if 0 not in row:
                break
            else:
                row.remove(0)
                poped += 1
                row.insert(0, -1)
    return board, poped


def playBoard(board):
    # print(board)
    count = 0
    while(1):
        popList = set()
        for row in range(len(board)-1):
            for col in range(len(board[0])-1):
                if isPop(board, row, col):
                    popList.add((row, col))
                    popList.add((row+1, col))
                    popList.add((row, col+1))
                    popList.add((row + 1, col+1))
        board, poped = pop(board, popList)
        # print(poped)
        count += poped

        if len(popList) == 0:
            break
    # print(count)
    return count


def solution(m, n, board):
    board = reverse(board)
    answer = playBoard(board)
    print(answer)
    return answer


solution(m, n, board)
