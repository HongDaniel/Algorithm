from collections import Counter

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    answer = []
    num_of_people = len(stages)  # 이용자
    stages.sort()
    mistake = Counter(stages).most_common()
    mistake.sort(key=lambda x: x[0])
    temp = {}
    cleared_people = 0
    for i in range(len(mistake)):  # 실패율 계산
        temp[mistake[i][0]] = mistake[i][1] / (num_of_people-cleared_people)
        cleared_people += mistake[i][1]

    for i in range(1, N+1):
        if i not in temp.keys():
            temp[i] = 0
    temp = sorted(temp.items())
    temp.sort(key=lambda x: x[1], reverse=True)
    for t in temp:
        if t[0] != N+1:
            answer.append(t[0])
    print(answer)
    return answer


solution(N, stages)
