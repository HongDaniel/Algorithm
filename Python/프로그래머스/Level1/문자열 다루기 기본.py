s = '00000'


def solution1(s):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    answer = True
    if(s[0] == '0') answer = False
    for i in range(len(s)):
        if(s[i] not in num):
            answer = False
            break

    return answer

# print(solution(s))


def solution2(s):
    return s.isdigit() and len(s) in (4, 6)
