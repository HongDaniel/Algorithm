n = 125


def solution(n):
    temp = []
    answer = 0
    while n > 0:
        mod, rest = divmod(n, 3)
        print(rest)
        temp.append(rest)
        n = mod
    for i in range(len(temp)):
        num = temp.pop()
        answer += (3**i)*num
    return answer


print(solution(n))
