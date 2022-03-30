N = 3
L = [[1, 1, 5, 3], [2, 3, 6, 6]]


def sortxy(L):
    newL = []
    for el in L:
        xar = [el[0], el[2]]
        yar = [el[1], el[3]]
        newL.append([(min(xar), max(xar)), (min(yar), max(yar))])
    newL.sort(key=lambda x: x[0][0])  # x 범위에 따른 분류
    return newL


def check_y(a, b):  # y범위가 겹치는지 확인
    tmp = [a, b]
    tmp.sort(key=lambda x: x[0])
    if tmp[0][1] >= tmp[1][0]:
        return True
    else:
        return False


def check_overlap(rec1, rec2):
    if rec1[0][1] >= rec2[0][0]:  # x 범위가 겹칠 때
        if check_y(rec1[1], rec2[1]):  # y 범위가 겹칠 때
            return True
        else:  # y 범위는 안겹칠 때
            return False
    else:
        return False


def solution(N, L):
    answer = 0
    newL = sortxy(L)
    overlap = False
    for i in range(len(newL)-1):
        rec1, rec2 = newL[i], newL[i+1]
        if check_overlap(rec1, rec2):
            overlap = True

    if overlap:
        print("overlap")
        return 1
    else:
        return 0


solution(N, L)
