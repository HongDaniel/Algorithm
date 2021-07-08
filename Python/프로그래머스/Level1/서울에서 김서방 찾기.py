def solution(seoul):
    num = 0
    for i in range(len(seoul)):
        if(seoul[i] == 'Kim'):
            num = i
            break
    answer = f"김서방은 {num}에 있다"
    return answer


def solution2(seoul):
    answer = f"김서방은 {seoul.index('Kim')}에 있다"
    return answer
