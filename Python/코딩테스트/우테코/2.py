log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]


def calculateTime(startTime, endTime):
    result = 0
    endTimeHour, endTimeMin = int(endTime[:2]), int(endTime[3:])
    startTimeHour, startTimeMin = int(startTime[:2]), int(startTime[3:])

    if endTimeMin >= startTimeMin:
        result += (endTimeHour-startTimeHour)*60 + (endTimeMin-startTimeMin)
    else:
        result += ((endTimeHour-1)-startTimeHour) * \
            60 + ((endTimeMin+60)-startTimeMin)
    return result


def solution(log):
    cnt = 0
    for i in range(0, len(log), 2):
        startTime = log[i]
        endTime = log[i+1]
        if calculateTime(startTime, endTime) >= 5:  # 5분 이상일 때만 카운트
            if calculateTime(startTime, endTime) >= 105:  # 105분 이상일 때는 105분
                cnt += 105
            else:
                cnt += calculateTime(startTime, endTime)

    # 공부한 시간(분)을 시간형태로 바꾸기
    studyHour = str(cnt//60).zfill(2)
    studyMin = str(cnt % 60).zfill(2)
    studyTime = studyHour+":"+studyMin
    print(studyTime)
    return studyTime


solution(log)
