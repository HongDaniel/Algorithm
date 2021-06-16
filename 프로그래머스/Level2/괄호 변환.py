p = "(()())()"


def isright(s):
    stack = []
    for l in s:
        if len(stack) == 0 and l == ')':
            return False
        if l == '(':
            stack.append(l)
        if stack[-1] == '(' and l == ')':
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''

    while(1):
        if len(p) == 0:  # 빈 문자열일 때
            print(p)
            return p
        if len(p) == len(answer):
            print(answer)
            return answer

        count = 0
        u, v = ('', '')
        for i in range(len(p)):  # u,v를 설정
            if p[i] == '(':
                count += 1
            elif p[i] == ')':
                count -= 1
            if count == 0:
                u = p[:i+1]
                v = p[i+1:]
                break
        print(f"u {u}")
        print(f"v {v}")

        if isright(u):  # u가 올바를 때
            p = v
            continue
        else:


solution(p)
