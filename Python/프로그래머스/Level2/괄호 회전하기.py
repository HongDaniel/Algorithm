s = "({[]})}{"


def solution(s):
    answer = 0
    # () {} [] 개수가 서로 안맞을 때
    if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
        return 0

    for i in range(len(s)):
        masterStack = []  # [], (), {}
        flag = True
        print(s)
        for al in s:
            if len(masterStack) == 0 and (al == ')' or al == '}' or al == ']'):
                flag = False
                break
            else:
                if al in ('(', '[', '{'):
                    masterStack.append(al)
                else:
                    if al == ')':
                        if '(' == masterStack[-1]:
                            masterStack.pop()
                        else:
                            flag = False
                            break
                    elif al == ']':
                        if '[' == masterStack[-1]:
                            masterStack.pop()
                        else:
                            flag = False
                            break
                    elif al == '}':
                        if '{' == masterStack[-1]:
                            masterStack.pop()
                        else:
                            flag = False
                            break
        if len(masterStack) != 0:
            flag = False
        if flag:
            answer += 1
        s = s[1:]+s[:1]
    print(answer)
    return answer


solution(s)
