# needs =
# [[1, 0, 0],
#  [1, 1, 0],
#  [1, 1, 0],
#  [1, 0, 1],
#  [1, 1, 0],
#  [0, 1, 1]]
r = 3
needs = [[]]


def solution(needs, r):
    answer = len(needs)
    col = [0]*16
    for row in range(len(needs)):
        for i in range(len(needs[row])):
            if needs[row][i] == 1:
                col[i] += 1
    # print(col)
    t = []
    for i in range(r):
        temp = max(col)
        t.append(col.index(temp))
        col[col.index(temp)] = 0
    # print(t)

    for row in range(len(needs)):
        for i in range(len(needs[row])):
            if i not in t:
                if needs[row][i] == 1:
                    answer -= 1

    print(answer)
    return answer


solution(needs, r)
