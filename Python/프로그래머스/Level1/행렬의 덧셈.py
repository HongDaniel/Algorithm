arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]


def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    answer = [[]for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            answer[row].append(arr1[row][col]+arr2[row][col])

    # print(answer)
    return answer


solution(arr1, arr2)
