num = 16


def solution(num):
    answer = 0
    while(num > 1):
        if(num % 2 == 0):  # 짝수일 경우
            num = num//2
            answer += 1
        else:  # 홀수일 경우
            num = num*3+1
            answer += 1
        if(answer == 500):
            answer = -1
            break
    # print(answer)
    return answer


solution(num)
