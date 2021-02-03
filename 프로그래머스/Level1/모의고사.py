import collections
import math
answers = [1, 3, 2, 4, 2]
# 가장 많은 문제를 맞힌 사람 = 틀린문제가 제일 적은 사람


def solution(answers):
    temp = answers
    an1 = []  # 1번 수포자
    an2 = []  # 2번 수포자
    an3 = []  # 3번 수포자
    ar1 = [1, 3, 4, 5]
    ar2 = [3, 1, 2, 4, 5]

    # 수열 선언부
    for i in range(1, len(temp) + 1):
        if((i % 5) != 0):
            an1.append(i % 5)
        else:
            an1.append(5)

    for i in range(len(temp)):
        if((i+1) % 2 != 0):
            an2.append(2)
        else:
            j = round((i+1)/2 - 1)
            t1 = ar1[j % 4]
            an2.append(t1)

    for i in range(len(temp)):
        if((i % 2) == 0):  # 홀수일때
            j = round((i/2))
            t1 = ar2[j % 5]
            an3.append(t1)
        else:  # 짝수일때
            an3.append(an3[i-1])
#######################################################

    cnt = []
    count = 0
    # print(an1)
    for i in range(len(temp)):
        if(temp[i] != an1[i]):
            count += 1
    cnt.append(count)
    count = 0

    for i in range(len(temp)):
        if(temp[i] != an2[i]):
            count += 1
    cnt.append(count)
    count = 0
    for i in range(len(temp)):
        if(temp[i] != an3[i]):
            count += 1
    cnt.append(count)

#####################################################
    answer = []
   # print(cnt)
    least = min(cnt)
    for i in range(3):
        if(cnt[i] == least):
            answer.append(i+1)
    # print(answer)
    return answer


solution(answers)
