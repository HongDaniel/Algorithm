C, F, X = 30, 2, 100


def solution(C, F, X):
    answer = 0.0
    n = 0  # n명의 알바생
    while True:
        # n+1명의 알바생을 고용했을 때 n명의 알바생을 고용했을 때보다 시간이 더 오래걸리면 탈출
        if C/(n*F+2) + X/((n+1)*F+2) > X/(n*F + 2):
            answer += X/(n*F + 2)
            break
        answer += C/(n*F + 2)
        n += 1

    answer = round(answer, 6)
    print(answer)
    return answer


solution(C, F, X)
