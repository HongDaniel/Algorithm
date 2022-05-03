r, c, k = map(int, input().split())
A = [[] for i in range(3)]
for i in range(3):
    A[i] = list(map(int, input().split()))

cnt = 0


def cal(ar):  # 개수를 카운트해서 새로운 행/열로 반환하는 함수
    els = set(ar)
    dic = {}
    tmp = []
    for el in els:
        if el != 0:
            dic[el] = ar.count(el)
    dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    for a, b in dic:
        tmp.append(a)
        tmp.append(b)
    return tmp


def reverse(ar):
    row, col = len(ar), len(ar[0])
    tmp = [[0]*row for i in range(col)]
    for i in range(row):
        for j in range(col):
            tmp[j][i] = ar[i][j]
    return tmp


def R(A, row):
    nar = [[] for i in range(row)]
    max_row = 0
    for i in range(row):
        nar[i] = cal(A[i])
        if len(nar[i]) > max_row:
            max_row = len(nar[i])
    for i in range(row):
        leftover = max_row-len(nar[i])
        tmp = [0]*leftover
        nar[i].extend(tmp)
    return nar


def C(A, col):
    A = reverse(A)
    A = R(A, len(A))
    A = reverse(A)
    return A


while(1):
    if cnt > 100:
        cnt = -1
        break
    row, col = len(A), len(A[0])
    if r-1 < row and c-1 < col and A[r-1][c-1] == k:
        break
    if row >= col:
        A = R(A, row)
    else:
        A = C(A, col)
    # print(A)
    cnt += 1

print(cnt)
