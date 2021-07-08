from collections import Counter
from copy import deepcopy

a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]


def solution(a, edges):
    answer = 0
    if sum(a) != 0:
        return -1
    copy_edge = deepcopy(edges)

    # 차수 조사
    level = []
    for edge in copy_edge:
        while edge:
            level.append(edge.pop())
    level = dict(Counter(level).most_common())
    # print(level)

    # print(f"edges: {edges}")
    # 흡수과정
    for edge in edges:
        el1 = edge[0]
        el2 = edge[1]

        if level[el1] <= level[el2]:
            answer += abs(a[el1])
            a[el2] += a[el1]
            a[el1] = 0

        else:
            answer += abs(a[el2])
            a[el1] += a[el2]
            a[el2] = 0

    print(answer)
    return answer

    if sum(a) != 0:
        return -1


solution(a, edges)
