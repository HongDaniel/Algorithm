arr = [3, 2, 6]
divisor = 10


def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if(len(answer) == 0):
        answer.append(-1)
    return answer


print(solution(arr, divisor))
