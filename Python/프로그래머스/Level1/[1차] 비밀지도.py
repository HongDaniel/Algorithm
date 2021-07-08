n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = [""for i in range(n)]
    b1 = []
    b2 = []

    # 2진수로 변환
    for i in range(len(arr1)):
        temp1 = bin(arr1[i])[2:]
        temp2 = bin(arr2[i])[2:]
        f1, f2 = 0, 0
        if len(temp1) != n:
            f1 = '0'*(n-len(temp1))+temp1
        else:
            f1 = temp1
        if len(temp2) != n:
            f2 = '0'*(n-len(temp2))+temp2
        else:
            f2 = temp2
        b1.append(f1)
        b2.append(f2)

    for row in range(n):
        for col in range(n):
            if b1[row][col] == '1' or b2[row][col] == '1':
                answer[row] += "#"
            else:
                answer[row] += " "

    print(answer)
    return answer


solution(n, arr1, arr2)
