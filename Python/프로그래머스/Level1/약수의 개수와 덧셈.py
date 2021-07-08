left = 13
right = 17


def demo(n):
    num = 0
    for i in range(1, n+1):
        if n % i == 0:
            num += 1
    return num


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if demo(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    print(answer)
    return answer


solution(left, right)
