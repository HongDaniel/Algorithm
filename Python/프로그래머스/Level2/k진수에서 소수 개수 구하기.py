n = 437674
k = 3


def n_dimension(n, k):  # n진수 변환 스트링으로 리턴
    tmp = ''
    while(1):
        if n < k:
            tmp = str(n)+tmp
            break
        tmp = str(n % k)+tmp
        n = n//k
    return tmp


def prime_check(n):  # 소수인지 확인 (숫자를 넘겨받음)
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    candis = n_dimension(n, k).split('0')
    answer = []
    for candi in candis:
        if candi and prime_check(int(candi)):
            answer.append(candi)
    print(candis)
    print(answer)
    return len(answer)


solution(n, k)
