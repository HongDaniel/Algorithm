
import math
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    # print(days)
    dday = days[0]
    count = 0
    for i in range(len(days)):
        if(days[i] <= dday):
            count += 1
        else:
            answer.append(count)
            count = 1
            dday = days[i]
        if(i == len(days)-1):
            answer.append(count)

    print(answer)
    return answer


solution(progresses, speeds)
