N = 100
M = 83


def getPrimeList(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    tmp = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if tmp[i] == True:
            for j in range(i+i, n, i):
                tmp[j] = False
    return [i for i in range(2, n) if tmp[i] == True]


def getPossible(primeList, M):
    cnt = 0
    partial_sum = 0
    right = 0

# 투포인터를 활용한 부분합 구하기
    for left in range(len(primeList)):
        while partial_sum < M and right < len(primeList):
            partial_sum += primeList[right]
            right += 1
    # 부분합이 m일 때 카운트 증가
        if partial_sum == M:
            cnt += 1
        partial_sum -= primeList[left]
    return cnt


def solution(N, M):
    primeList = getPrimeList(N)
    answer = getPossible(primeList, M)
    return answer


solution(N, M)
