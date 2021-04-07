arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr1_col = len(arr1[0])
    arr2_col = len(arr2[0])
    answer = [[0 for j in range(arr2_col)] for i in range(arr1_row)]
    # print(f"{arr1_row} {arr1_col} {arr2_row} {arr2_col}")

    for row1 in range(arr1_row):
        for col2 in range(arr2_col):
            for i in range(arr1_col):
                answer[row1][col2] += arr1[row1][i]*arr2[i][col2]
    print(answer)
    return answer


solution(arr1, arr2)
