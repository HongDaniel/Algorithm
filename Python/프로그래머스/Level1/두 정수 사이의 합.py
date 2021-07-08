def solution(a, b):
    if(a > b):
        a, b = b, a
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer


print(solution(-3, 4))
