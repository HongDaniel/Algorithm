citations = [3, 0, 6, 1, 5]


def solution1(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if(citations[i] <= i):
            answer = i
            break
    if(citations[0] == 0):
        answer = 0
    elif(answer == 0):
        answer = len(citations)
    print(answer)
    return answer


def solution2(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if(citations[i] <= i):
            return i
    return len(citations)
