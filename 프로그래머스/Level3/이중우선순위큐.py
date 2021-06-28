import re
operations = ["I 7", "I 5", "I -5", "D -1"]


def solution(operations):
    answer = []
    temp = []
    for idx, op in enumerate(operations):
        operations[idx] = re.split(' ', operations[idx])
        if operations[idx][0] == 'I':  # 원소 삽입
            temp.append(int(operations[idx][1]))
        elif operations[idx][0] == 'D' and operations[idx][1] == '1':  # 최댓값 삭제
            if temp:
                temp.pop(temp.index(max(temp)))
        elif operations[idx][0] == 'D' and operations[idx][1] == '-1':  # 최댓값 삭제
            if temp:
                temp.pop(temp.index(min(temp)))

    if temp:
        answer.append(max(temp))
        answer.append(min(temp))
    else:
        return [0, 0]
    print(answer)
    return answer


solution(operations)
