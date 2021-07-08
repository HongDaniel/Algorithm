s = " 3people  unFollowed me"


def solution(s):
    answer = ''
    s = list(s.lower())

    for i in range(len(s)):
        if(i == 0):
            s[i] = s[i].upper()
        else:
            if(s[i-1] == ' '):
                s[i] = s[i].upper()
    answer = "".join(s)
    print(answer)
    return answer


solution(s)
