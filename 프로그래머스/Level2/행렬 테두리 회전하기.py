rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]


def solution(rows, columns, queries):
    answer = []
    board = [[] for i in range(rows)]  # 초기화
    for i in range(rows):
        for j in range(columns):
            board[i].append((j+1)+columns*i)

    for q in queries:
        top, left, bottom, right = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        tmp = board[top][left]
        changed = []
        for y in range(top, bottom):  # 왼쪽
            board[y][left] = board[y+1][left]
            changed.append(board[y][left])

        for x in range(left, right):  # 아래
            board[bottom][x] = board[bottom][x+1]
            changed.append(board[bottom][x])

        for y in range(bottom, top, -1):  # 오른쪽
            board[y][right] = board[y-1][right]
            changed.append(board[y][right])

        for x in range(right, left, -1):  # 위
            board[top][x] = board[top][x-1]
            changed.append(board[top][x])
        board[top][left+1] = tmp
        changed.append(tmp)
        answer.append(min(changed))
        # print(changed)
    print(answer)
    return answer


solution(rows, columns, queries)
