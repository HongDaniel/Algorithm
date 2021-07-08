land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]


def solution(land):
    answer = 0

    for row in range(1, len(land)):
        for i in range(4):
            land[row][i] += max(land[row-1][:i] + land[row-1][i+1:])
    # print(land[-1])
    answer = max(land[-1])
    print(answer)
    return answer


solution(land)


def solution2(land):
    answer = max(land[0])  # 1번 째 행에서 가장 큰 수
    pre_num_of_max = land[0].count(max(land[0]))  # 가장 큰 수의 개수
    pre = land[0].index(max(land[0]))  # 1번 째 행에서 가장 큰 열

    for row in land[1:]:
        index = row.index(max(row))  # 가장 큰 열의 인덱스
        if pre != index or pre_num_of_max > 1:
            answer += max(row)
            pre = index
            pre_num_of_max = row.count(max(row))
        else:
            temp = list(row)
            temp.remove(max(row))
            nextbig = max(temp)
            pre = row.index(nextbig)
            pre_num_of_max = row.count(nextbig)
            answer += nextbig
        # print(f"pre: {pre} numofpre: {pre_num_of_max}")

    print(answer)
    return answer
