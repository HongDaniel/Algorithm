key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(key, m):  # 키를 회전하는 작업
    newKey = [[0]*m for i in range(m)]
    for row in range(m):
        for col in range(m):
            newKey[row][col] = key[col][(m-1)-row]
    return (newKey)


def check(newLength, lock, key, start, end, n, m, row, col):
    board = [[0]*newLength for i in range(newLength)]  # 새로운 판

    for x in range(n):  # lock초기화 작업
        for y in range(n):
            board[x+start][y+start] += lock[x][y]

    for x in range(m):  # key를 더한다
        for y in range(m):
            board[x+row][y+col] += key[x][y]

    for x in range(start, end):
        for y in range(start, end):
            if board[x][y] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    n, m = len(lock[0]), len(key[0])  # lock:n key:m
    newLength = n+(m-1)*2
    checkLength = newLength-(m-1)
    start = m-1  # 2
    end = newLength-m+1  # 5
    for case in range(0, 4):  # 해당 키로 로테이션
        # print(f"key:{key}")
        for row in range(0, end):
            for col in range(0, end):
                if check(newLength, lock, key, start, end, n, m, row, col):
                    answer = True
        key = rotate(key, m)

    print(answer)
    return answer


solution(key, lock)
