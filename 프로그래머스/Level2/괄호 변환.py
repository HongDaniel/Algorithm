p = "()))((()"


def correct(p):  # 올바른 문자열 확인 ok
    tmp = 0
    for l in p:
        if l == '(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return False
    if tmp == 0:
        return True
    else:
        return False


def divide(p):  # u,v 나누는 과정 ok
    if len(p) == 0:
        return ''
    dec = 0
    for i in range(len(p)):
        if p[i] == '(':
            dec += 1
        else:
            dec -= 1

        if dec == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v


def reverse(u):
    u = list(u[1:-1])
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    u = "".join(u)
    return u


def recursive(s):
    if s == '':  # 1단계
        return ''
    u, v = divide(s)  # 2단계
    # print(f"u: {u} v: {v}")
    if correct(u):  # u가 올바른 문자열일 때
        return u+recursive(v)

    else:  # u가 아닐때
        return '(' + recursive(v) + ')' + reverse(u)


def solution(p):
    return p if correct(p) else recursive(p)


solution(p)
