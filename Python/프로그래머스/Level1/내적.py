a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]


def solution(a, b):
    answer = 0
    for a, b in zip(a, b):
        answer += a*b
    print(answer)
    return answer


solution(a, b)
