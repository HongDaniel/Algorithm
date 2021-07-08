x = 11


def solution(x):
    answer = ''
    temp = []
    x2 = x
    while(x > 0):
        temp.append(x % 10)
        x = x//10

    if(x2 % sum(temp) == 0):
        answer = True
    else:
        answer = False
    return answer


solution(x)
