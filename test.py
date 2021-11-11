# from itertools import combinations as C
v = [[1, 4], [3, 4], [3, 10]]


def solution(v):
    answer = []
    arx = []
    ary = []
    for el in v:
        arx.append(el[0])
        ary.append(el[1])
    print(arx)
    print(ary)
    setX = set(arx)
    setY = set(ary)
    print(setX)
    missingx = 0
    missingy = 0
    for x, y in zip(setX, setY):
        if arx.count(x) == 1:
            missingx = x
        if ary.count(y) == 1:
            missingy = y
    return [missingx, missingy]


solution(v)
