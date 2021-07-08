n = 118372


def solution(n):
    temp = list(str(n))
    temp.sort()
    # print(temp)
    answer = ""
    for i in range(len(temp)):
        answer += temp.pop()
    # print(answer)
    return int(answer)


solution(n)
