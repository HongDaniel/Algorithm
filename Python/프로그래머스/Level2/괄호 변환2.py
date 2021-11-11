p = "()))((()"
converted = {'(': 1, ')': -1}


def Seperate(p):
    check = converted[p[0]]
    u, v = '', ''
    for i in range(1, len(p)):
        check += converted[p[i]]
        if check == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v


def isCorrect(p):
    check = 0
    for letter in p:
        check += converted[letter]
        if check < 0:
            return False
    if check != 0:
        return False
    else:
        return True


def recursive(p):
    if p == '':  # 1 단계
        return ''
    u, v = Seperate(p)  # 2 단계

    if isCorrect(u):  # u가 올바른 문자열이라면
        return u + recursive(v)
    else:
        return stageFour(u, v)


def reverse(u):
    newString = ''
    for i in range(0, len(u)):
        if u[i] == '(':
            newString += ')'
        else:
            newString += '('
    return newString


def stageFour(u, v):
    return '('+recursive(v)+')'+reverse(u[1:-1])


def solution(p):
    if p == '':  # 1 단계
        return ''
    if isCorrect(p):
        return p
    else:
        return recursive(p)


print(solution(p))
