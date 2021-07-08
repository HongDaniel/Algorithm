import string
s = 'Z'
n = 4


def solution(s, n):
    answer = ''
    low = list(string.ascii_lowercase)  # 소문자 배열 26자리 0~25
    upper = list(string.ascii_uppercase)  # 대문자 배열

    for i in range(len(s)):
        if(s[i] == ' '):
            answer += ' '
        elif(s[i] in low):
            if(low.index(s[i])+n <= 25):
                answer += low[low.index(s[i])+n]
            else:
                answer += low[low.index(s[i])+n-26]

        elif(s[i] in upper):
            if(upper.index(s[i])+n <= 25):
                print(upper.index(s[i]))
                answer += upper[upper.index(s[i])+n]
            else:
                answer += upper[upper.index(s[i])+n-26]
    return answer


print(solution(s, n))
