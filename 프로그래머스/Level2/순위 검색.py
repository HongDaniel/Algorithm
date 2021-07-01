import re
from itertools import combinations as combi
from collections import defaultdict

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]


query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


def solution(info, query):
    answer = []

    infodict = defaultdict(list)
    for i in info:
        temp = i.split(" ")
        keylist = temp[:-1]
        score = int(temp[-1])

        for j in range(5):
            for c in combi(keylist, j):
                key = ''.join(c)
                infodict[key].append(score)

    for key in infodict.keys():  # 같은 key값이면 점수를 오름차순 정렬
        infodict[key].sort()
    print(infodict.keys())

    for q in query:  # query 정보 분리
        temp = []
        q = q.split(" ")

        for el in q:
            if el != 'and' and el != '-':
                temp.append(el)

        key = ''.join(temp[:-1])
        score = int(temp[-1])

        count = 0  # 조건에 해당하는 info

        if key in infodict.keys():
            value = infodict[key]  # value는 배열
            start, end = 0, len(value)
            while start <= end and start < len(value):
                mid = (start+end)//2

                if value[mid] < score:
                    start = mid+1
                else:
                    end = mid-1
            count = len(value)-start
        answer.append(count)

    # print(temp)
    # print(answer)
    return answer


solution(info, query)


# 정확성만 만족시킨 코드


def solution2(info, query):
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
            if int(query[i][4]) > int(info[j][4]):
                flag = False

            if flag:
                for k in range(4):
                    if '-' in query[i][k]:
                        continue
                    if query[i][k] != info[j][k]:
                        flag = False
                        break
            if flag:
                temp += 1
        answer.append(temp)
    print(answer)
    return answer
