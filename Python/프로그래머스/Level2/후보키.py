from itertools import combinations as combi
relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]


def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    # print(f"rows: {rows} cols: {cols}")

    candidates = []  # 후보키가 될 수 있는 요소들
    for i in range(1, cols+1):
        candidates.extend(combi(range(cols), i))
    # print(candidates)

    # 유일성 test
    unique = []
    for keys in candidates:
        keycheck = set()
        for row in range(rows):
            temp = ""
            for col in keys:
                temp += relation[row][col]
            keycheck.add(temp)
        if len(keycheck) == rows:
            unique.append(keys)

    for i in range(len(unique)):
        unique[i] = list(unique[i])
    # print(unique)
    answer = set()

    # 최소성 test
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            temp2 = []
            for el in unique[i]:
                if el in unique[j]:
                    temp2.append(el)
            if len(temp2) == len(unique[i]):
                answer.add(tuple(unique[j]))

    print(len(unique)-len(answer))
    return len(unique)-len(answer)


solution(relation)
