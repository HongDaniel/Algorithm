s = 'babaa'

# stack의 개념을 활용한 풀이


def solution(s):
    answer = 0
    stack = [s[0]]
    for al in s[1:]:
        if(stack):
            top = stack[-1]
            if(top == al):
                stack.pop()
            else:
                stack.append(al)
        else:
            stack.append(al)

    if(len(stack) == 0):
        answer = 1
    return answer


solution(s)
