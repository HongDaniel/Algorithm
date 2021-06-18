from collections import deque
p = "()))((()"


def is_correct(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack


def detatch(string):  # u, v로 분리
    str_que = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while str_que:  # 큐사용
        u += str_que.popleft()
        if u[-1] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break  # 균형 잡힌 괄호

    v = ''.join(list(str_que))
    return u, v


def reverse(u):  # 뒤집기
    return ''.join([')' if s == '(' else '('for s in u])


u = "))(("
print(reverse(u[1:-1]))


def recursive(string):
    if string == '':  # 1번
        return ''
    u, v = detatch(string)  # 2번
    if is_correct(u):  # 3번
        return u + recursive(v)
    else:  # 4번
        return '(' + recursive(v) + ')' + reverse(u[1:-1])


def solution(p):
    if is_correct(p):
        print(p)
    else:
        print(recursive(p))
