N = int(input())
board = [[0]*N for i in range(N)]  # 배치도
info = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
wishList = {}

for i in range(N*N):
    info.append(list(map(int, input().split())))


def findMax(ar):
    num = 0
    for row in ar:
        if max(row) > num:
            num = max(row)
    return num


def search(ar, num):  # num을 갖고 있는 (행,열)들을 리턴
    tmp = []
    for row in range(N):
        for col in range(N):
            if ar[row][col] == num and board[row][col] == 0:
                tmp.append((row, col))
    return tmp


def check1(s, like):  # 좋아하는 학생이 가장 많은 칸
    satisfy = []
    check = [[0]*N for i in range(N)]

    for row in range(N):  # 행
        for col in range(N):  # 열
            cnt = 0
            if board[row][col] == 0:
                for i in range(4):
                    if 0 <= row+dx[i] < N and 0 <= col+dy[i] < N:  # 해당 칸이 있을 경우
                        if board[row+dx[i]][col+dy[i]] in like:
                            cnt += 1
            check[row][col] = cnt
    # print(f"check:{check}")
    most = findMax(check)  # 좋아하는 학생이 가장 많은 수
    satisfy = search(check, most)  # most와 일치하는 칸
    return satisfy


def check2(ar1):  # 인근에 빈칸이 가장 많은 칸
    temp = {}
    ar2 = []
    for (row, col) in ar1:
        cnt = 0
        for i in range(4):
            if 0 <= row+dx[i] < N and 0 <= col+dy[i] < N:  # 칸이 유효
                if board[row+dx[i]][col+dy[i]] == 0:
                    cnt += 1
        temp[(row, col)] = cnt
    most = max(temp.values())
    for key in temp:
        if temp[key] == most:
            ar2.append(key)
    return ar2


def check3(ar2):
    return sorted(ar2, key=lambda x: (x[0], x[1]))


def dispatch(s, like):  # 학생배치
    ar1 = check1(s, like)
    # print(f"ar1:{ar1}")
    if len(ar1) == 1:
        x, y = ar1[0][0], ar1[0][1]
        board[x][y] = s
    else:
        ar2 = check2(ar1)
        # print(f"ar2:{ar2}")

        if len(ar2) == 1:
            x, y = ar2[0][0], ar2[0][1]
            board[x][y] = s
        else:
            ar3 = check3(ar2)
            # print(f"ar3:{ar3}")
            x, y = ar3[0][0], ar3[0][1]
            board[x][y] = s
    # print(f"board:{board}")


def getScore(row, col):
    cnt = 0
    like = wishList[board[row][col]]
    for i in range(4):
        if 0 <= row+dx[i] < N and 0 <= col+dy[i] < N:
            if board[row+dx[i]][col+dy[i]] in like:
                cnt += 1
    if cnt < 1:
        return 0
    elif cnt < 2:
        return 1
    elif cnt < 3:
        return 10
    elif cnt < 4:
        return 100
    else:
        return 1000


for ar in info:  # 자리배치
    s = ar[0]
    like = ar[1:]
    wishList[s] = like
    dispatch(s, like)
# print(f"board:{board}")
score = 0
for row in range(N):  # 행
    for col in range(N):  # 열
        score += getScore(row, col)
print(score)
