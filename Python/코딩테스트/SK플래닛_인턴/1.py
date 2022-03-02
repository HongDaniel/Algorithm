t = [1, 1, 2, 6]
m = 3


def solution(t, m):
    answer = 0
    t.sort()  # 정렬
    for i in range(m):
        answer += t[i]+1
    print(answer)
    return answer


solution(t, m)
