p = ">><"


def solution(p):
    answer = 0
    isLeft = False
    isRight = False
    startCnt = 0

    for i in range(len(p)):
        # print(p[i])

        if i == 0 and p[i] == "<":
            answer += 1
            isLeft = True
            continue

        if isLeft and p[i] == "<":
            answer += 1
            continue

        if p[i] == ">":
            isLeft = False
            startCnt += 1
            isRight = True
            continue

        if isRight == True and p[i] == "<":
            startCnt = 0
            isRight = False
            continue

        if p[i] == "<":
            continue

    print(answer + startCnt)
    return answer + startCnt


solution(p)
