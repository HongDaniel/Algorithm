from itertools import combinations as C
relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

ar = [n for n in range(len(relation[0]))]
print(list(C(ar, 3)))
