import string
import re


def solution(new_id):
    temp = new_id
    temp = temp.lower()  # 1단계
    temp = list(temp)
    answer = []

    s = ['-', '_', '.']
    for i in range(len(temp)):  # 2단계
        if temp[i] in string.ascii_lowercase or temp[i] in string.digits or temp[i] in s:
            answer.append(temp[i])
        else:
            pass
    temp = answer
    answer = list(temp[0])
    count = 0

    for i in range(1, len(temp)):  # 3단계
        if temp[i] != temp[i-1]:
            answer.append(temp[i])
        else:
            if temp[i] == '.':
                pass
            else:
                answer.append(temp[i])

    while True:  # 4단계
        if len(answer) == 0:
            break
        if answer[0] != '.' and answer[-1] != '.':
            break
        else:
            if answer[0] == '.':
                answer.pop(0)
                if len(answer) == 0:
                    break
            if answer[-1] == '.':
                answer.pop(-1)

    if len(answer) == 0:  # 5단계
        answer.append('a')

    if len(answer) >= 16:  # 6단계
        answer = answer[:15]

    while True:  # 4단계 (다시)
        if answer[0] != '.' and answer[-1] != '.':
            break
        else:
            if answer[0] == '.':
                answer.pop(0)
            if answer[-1] == '.':
                answer.pop(-1)

    while True:  # 7단계
        if len(answer) > 2:
            break
        else:
            answer.append(answer[-1])

    return ''.join(answer)


# print(solution("abcdefghijklmn.p"))

# re.sub(pattern, replace, string) 형태


def solution2(new_id):
    st = new_id
    st = st.lower()  # 1
    st = re.sub('[^a-z0-9A-Z\-._]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    if len(st) > 2:
        pass
    else:
        while len(st) >= 3:
            st += st[-1]
    return st


print(solution2("abcdefghijklmn.p"))
