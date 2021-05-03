s = "110010101001"


def solution(s):
    answer = []
    zeroCount = 0
    count = 0
    while(1):
        if '1' == s:
            break
        newS = 0
        for al in s:
            if al == '1':
                newS += 1
            elif al == '0':
                zeroCount += 1
        s = str(bin(newS))[2:]
        count += 1
    answer.append(count)
    answer.append(zeroCount)
    print(answer)
    return answer


solution(s)
