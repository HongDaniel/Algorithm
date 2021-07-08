n = 5


def solution(n):
    num = ['1', '2', '4']
    answer = ''
    if(n < 4):
        answer += num[n-1]
    else:
        a, b = divmod(n-1, 3)
        answer += solution(a)+num[b]
    print(answer)
    return answer


solution(n)
