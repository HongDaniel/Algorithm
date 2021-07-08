n = 3


def solution(n):
    answer = [0, 1]
    for i in range(2, n+1):
        # print(i)
        answer.append(answer[i-1]+answer[i-2])
    print(answer)
    return answer[-1] % 1234567


solution(n)
