arr = [10]


def solution(arr):
    answer = []
    arr.remove(min(arr))
    if(arr):
        answer = arr
    else:
        answer.append(-1)
    # print(answer)
    return answer


solution(arr)
