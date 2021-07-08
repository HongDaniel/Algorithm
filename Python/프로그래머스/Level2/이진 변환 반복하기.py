s = "110010101001"


def solution(s):
    answer = []
    zeroCount = 0
    count = 0
    while(1):
        if '1' == s:
            break
        newS = s.count('1')
        zeroCount += s.count('0')
        s = str(bin(newS))[2:]  # 1의 길이를 2진 변환
        count += 1
    answer.append(count)
    answer.append(zeroCount)
    print(answer)
    return answer


solution(s)
