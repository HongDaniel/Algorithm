arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
    0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]
nums = []


def divide(arr):
    new1, new2, new3, new4 = [[] for i in range(len(arr)//2)], [[] for i in range(
        len(arr)//2)], [[] for i in range(len(arr)//2)], [[] for i in range(len(arr)//2)]
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if row < len(arr)//2:
                if col < len(arr)//2:
                    new1[row].append(arr[row][col])
                else:
                    new2[row].append(arr[row][col])
            else:
                if col < len(arr)//2:
                    new3[row-len(arr)//2].append(arr[row][col])
                else:
                    new4[row-len(arr)//2].append(arr[row][col])
    return new1, new2, new3, new4


def check(arr):  # 2차원 배열의 모든 원소가 같은지 확인
    tmp = arr[0][0]
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] != tmp:
                return False
    return True


def recursive(arr):
    if len(arr) == 1 or check(arr):
        nums.append(arr[0][0])
        return
    else:
        ar1, ar2, ar3, ar4 = divide(arr)
        tmp = [ar1, ar2, ar3, ar4]
        for i in range(4):
            if check(tmp[i]):
                nums.append(tmp[i][0][0])
            else:
                recursive(tmp[i])
                pass


def solution(arr):
    answer = []
    recursive(arr)
    answer.append(nums.count(0))
    answer.append(nums.count(1))
    print(answer)
    return answer


solution(arr)
