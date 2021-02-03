import math
n = 10


def isprimenum(n):
    if(n == 2):
        return True
    elif(n == 3):
        return True
    elif(n % 2 == 0):
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if(n % i == 0):
                return False
    return True


def solution(n):
    answer = 0
    for i in range(2, n+1):
        if(isprimenum(i)):
            answer += 1
        else:
            pass
    return answer


print(solution(n))
