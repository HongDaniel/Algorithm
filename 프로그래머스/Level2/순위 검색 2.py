from itertools import combinations as combi
import collections

infos = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]


query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


def solution(infos, query):
    answer = []
    info_dict = {}
    for info in infos:
        info = info.split(' ')
        info_key = info[:-1]
        info_value = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):
                tmpkey = "-".join(c)
                info_dict[tmpkey] = info_value

    print(info_dict)
    print(answer)
    return answer


solution(infos, query)
