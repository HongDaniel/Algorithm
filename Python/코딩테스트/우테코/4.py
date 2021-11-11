s = "aaaaabbaab"


def connect(s):
    back_repeated = 0
    for i in range(len(s)-1, -1, -1):
        if s[0] == s[i]:
            back_repeated += 1
        else:
            break
    newS = (s[0]*back_repeated)+s[:-back_repeated]
    # print(newS)
    return newS


def cutter(s):
    ar = []
    cnt = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ar.append(cnt)
            cnt = 1
        if i+1 == len(s)-1:
            ar.append(cnt)
    return ar


def solution(s):
    answer = []
    if s[0] != s[-1]:
        answer = cutter(s)
    else:
        answer = cutter(connect(s))
    # answer.sort()
    print(answer)
    return answer


solution(s)
