s = "abde"


def solution(s):
    answer = ''
    slen = len(s)
    if(slen % 2 != 0):
        answer = s[slen//2]
    else:
        answer = s[(slen//2)-1] + s[slen//2]
    return answer


print(solution(s))
