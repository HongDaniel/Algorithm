from itertools import combinations as C
arr = [2, 5, 3, 8, 1]
k = 3
t = 11


def solution(arr, k, t):
    answer = 0
    for n in range(k, len(arr)+1):
        candis = list(C(arr, n))
        for candi in candis:
            if sum(candi) <= t:
                print(candi)
                answer += 1
    print(answer)
    return answer


solution(arr, k, t)
