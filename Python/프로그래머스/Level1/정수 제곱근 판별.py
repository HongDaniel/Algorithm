import math
n = 121


def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    if(sqrt % 1 == 0):
        answer = int((sqrt+1)**2)
    else:
        answer = -1
    return answer


print(solution(n))
