arr = [2, 1, 3, 1, 2, 1]


def solution(arr):
    answer = []
    countElement = [arr.count(1), arr.count(2), arr.count(3)]
    maxElement = max(countElement)
    for el in countElement:
        answer.append(maxElement-el)
    print(answer)
    return answer


solution(arr)
