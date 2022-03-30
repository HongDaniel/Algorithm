n = 5
clockwise = True
# 5	true	[[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]
# 6	false	[[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]
# 9	false	[[1,8,7,6,5,4,3,2,1],[2,9,14,13,12,11,10,9,8],[3,10,15,18,17,16,15,14,7],[4,11,16,19,20,19,18,13,6],[5,12,17,20,21,20,17,12,5],[6,13,18,19,20,19,16,11,4],[7,14,15,16,17,18,15,10,3],[8,9,10,11,12,13,14,9,2],[1,2,3,4,5,6,7,8,1]]


def dfs(board, x, y, i, wise):
    dx = [0, 1, 0, -1]  # 동 남 서 북
    dy = [1, 0, -1, 0]
    assign = 1
    fill_length = len(board)-1

    t = 5
    while(1):
        if fill_length <= 1:
            board[x][y] = assign
            break

        # print(f"fill_length: {fill_length}")
        for j in range(fill_length):  # 8
            board[x][y] = assign
            assign += 1
            if j != fill_length-1:
                x = x+dx[i]
                y = y+dy[i]

        #  방향을 튼다
        fill_length -= 2
        if wise == 'left':
            i = (i-1) % 4
            x = x+dx[i]
            y = y+dy[i]
        elif wise == 'right':
            i = (i+1) % 4
            x = x+dx[i]
            y = y+dy[i]

        # t -= 1

    # for el in board:
    #     print(el)


def fill_clockwise(board, n):
    dfs(board, 0, 0, 0, 'right')
    dfs(board, 0, n-1, 1, 'right')
    dfs(board, n-1, 0, 3, 'right')
    dfs(board, n-1, n-1, 2, 'right')
    return board


def fill_counterwise(board, n):
    dfs(board, 0, 0, 1, 'left')
    dfs(board, 0, n-1, 2, 'left')
    dfs(board, n-1, 0, 0, 'left')
    dfs(board, n-1, n-1, 3, 'left')
    return board


def solution(n, clockwise):
    board = [[0]*n for i in range(n)]
    if clockwise:
        board = fill_clockwise(board, n)
    else:
        board = fill_counterwise(board, n)

    for el in board:
        print(el)


solution(n, clockwise)
