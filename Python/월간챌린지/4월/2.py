s = "(())"


def solution(s):
    answer = 0

    # 개수가 아예 안맞을 경우
    if s.count('[') != s.count(']') or s.count('(') != s.count(')') or s.count('{') != s.count('}'):

        return 0

    for i in range(len(s)):  # x
        if i >= 1:
            s = s[1:]+s[0]

        flag = True

        # stack 사용
        temp = list(s)

        for i in range(len(s)):
            # print(f"temp:{temp}")

            if s[i] == '(':
                if ')' not in s[i+1:]:
                    flag = False
                    break
                else:
                    if ')' in temp and temp.index('(') < temp.index(')'):
                        temp.pop(temp.index(')'))
                    else:
                        flag = False
                        break

            elif s[i] == '[':
                if ']' not in s[i+1:]:
                    flag = False
                    break
                else:
                    if ']' in temp and temp.index('[') < temp.index(']'):
                        temp.pop(temp.index(']'))
                    else:
                        flag = False
                        break

            elif s[i] == '{':
                if '}' not in s[i+1:]:
                    flag = False
                    break
                else:
                    if '}' in temp and temp.index('{') < temp.index('}'):
                        temp.pop(temp.index('}'))
                    else:
                        flag = False
                        break

        if len(temp) != len(s)//2:
            flag = False
        if flag:
            answer += 1
        print(f"s:{s} {flag}")

    print(answer)
    return answer


solution(s)
