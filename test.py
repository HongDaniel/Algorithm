import re
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


def binary_search(score, info):
    left, right = 0, len(info)-1
    while left <= right:
        middle = (left+right)//2
        if int(info[middle-1][-1]) < score and int(info[middle+1][-1]) > score:
            # print(middle)
            return middle
        else:
            if int(info[middle][-1]) > score:
                left = middle+1
            elif int(info[middle][-1]) < score:
                right = middle-1
            else:
                # print(middle)
                return middle
    print('나옴')
    return middle


def solution(info, query):
    answer = []
    for idx, inf in enumerate(info):
        info[idx] = inf.split(' ')
    info.sort(key=lambda x: int(x[-1]))
    # print(info)

    for q in query:
        # query 리스트로 나누기
        q = q.split(' and ')
        last = q[-1].split(' ')
        q.pop()
        q.extend(last)
        language, field, exp, food, score = q[0], q[1], q[2], q[3], int(q[4])

        cnt = 0
        for inf in info:  # 응시자 정보에서 찾기
            if (inf[0] == language or language == '-') and (inf[1] == field or field == '-') and (inf[2] == exp or exp == '-') and (inf[3] == food or food == '-') and int(inf[4]) >= score:
                cnt += 1
        answer.append(cnt)
    print(answer)
    return answer


solution(info, query)
