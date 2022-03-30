n = 4


def solution(n):
    if n == 1 or n == 2:
        return 1

    cnt = 0
    for i in range(1, n):
        cnt += (solution(i)*solution(n-i))
    return cnt


print(solution(n))
