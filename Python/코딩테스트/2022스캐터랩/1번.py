data = [[4, 0, 12], [1, 0, 16], [3, 0, 18], [
    3, 0, 17], [2, 0, 15], [3, 2, 22], [2, 1, 17]]


def getBestday(day_score):  # 소개팅하기 가장 좋은 날 구하기
    priority = ['토', '금', '일', '수', '목', '화', '월']  # 우선순위
    bestScore = day_score[0][1][0]
    candis = []  # 후보군
    for score in day_score:
        if score[1][0] == bestScore:
            candis.append(score)
        else:  # 최고 점수보다 1점이라도 낮으면 break
            break

    if len(candis) == 1:
        return candis[0][0]
    else:  # 동점일 경우
        for day in priority:
            for el in candis:
                if day == el[0]:
                    return day


def getWorstday(day_score):  # 소개팅하기 가장 안좋은 날 구하기
    priority = ['월', '화', '목', '수', '일', '금', '토']
    candis = []  # 후보군
    worstScore = day_score[-1][1][0]
    for i in range(len(day_score)-1, -1, -1):
        if day_score[i][1][0] == worstScore and day_score[i][1][1] == True:
            candis.append(day_score[i])
    print(candis)
    if len(candis) == 0:
        return '없음'

    elif len(candis) == 1:
        return candis[0][0]

    else:
        for day in priority:
            for el in candis:
                if day == el[0]:
                    return day


def getScore(el):
    score = 0
    sky, rain, temp = el
    canBeWorst = False
    if temp >= 30 or temp <= 0:
        canBeWorst = True
    score += 20-abs(22-temp)  # 온도에 해당하는 점수
    if rain == 0:  # 강수: 없음
        if sky == 1:  # 하늘:맑음
            score += 20
        elif sky == 2:  # 하늘:구름조금
            score += 20
        elif sky == 3:  # 하늘:구름많음
            score += 17
        elif sky == 4:  # 하늘:흐림
            score += 10
            canBeWorst = True
    elif rain == 1:  # 강수:비
        score += 5
        canBeWorst = True
    elif rain == 2:  # 강수: 눈
        score += 14
    return (score, canBeWorst)


def solution(data):
    answer = []
    day_score = {}
    idx_day = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
    day_idx = {'월': 0, '화': 1, '수': 2, '목': 3,
               '금': 4, '토': 5, '일': 6}
    # 월~일 점수 구하기
    for i in range(len(data)):
        day_score[idx_day[i]] = getScore(data[i])

    # 점수 내림차순으로 정렬
    day_score = sorted(day_score.items(),
                       key=lambda item: item[1][0], reverse=True)
    # 가장 좋은날 안좋은 날 구하기
    bestDay = day_idx[getBestday(day_score)]
    if getWorstday(day_score) == '없음':
        worstDay = -1
    else:
        worstDay = day_idx[getWorstday(day_score)]
    answer = [bestDay, worstDay]
    print(answer)
    return answer


solution(data)
