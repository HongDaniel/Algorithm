import re

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]


query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


def solution(info, query):
    answer = []

    for i in range(len(info)):  # info 정보 분리
        info[i] = info[i].split(' ')
    print(info)

    for i in range(len(query)):  # query 정보 분리
        query[i] = query[i].split(' and ')
        change = query[i].pop(-1)
        query[i].append(''.join(re.findall('[a-zA-Z\-]', change)))
        query[i].append(''.join(re.findall('\d', change)))
    print(query)

    for i in range(len(query)):
        temp = 0
        for j in range(len(info)):
            flag = True
            for k in range(4):
                if '-' in query[i][k]:
                    continue
                if query[i][k] != info[j][k]:
                    flag = False
                    continue
            if int(query[i][4]) > int(info[j][4]):
                flag = False
            if flag:
                temp += 1
        answer.append(temp)

    print(answer)
    return answer


solution(info, query)
