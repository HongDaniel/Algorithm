s = "aabbaccc"


def solution(s):
    answer = len(s)
    words = []
    for length in range(1, len(s)//2+2):  # n개의 숫자로 문자열을 자른 결과
        words.append(list(s[i:i+length] for i in range(0, len(s), length)))
    print(words)

    for pattern in words:  # n개의 문자의 패턴
        # print(pattern)
        pre = pattern[0]
        cnt = 1
        newpattern = ""
        for i in range(1, len(pattern)):
            if pattern[i] == pre:
                cnt += 1
            else:
                if cnt > 1:
                    newpattern += str(cnt)+pre
                    pre = pattern[i]
                else:
                    newpattern += pre
                cnt = 1
                pre = pattern[i]

            if i == len(pattern)-1:
                if cnt == 1:
                    newpattern += pattern[i]
                else:
                    newpattern += str(cnt)+pre
        print(newpattern)
        if len(newpattern) < answer and len(newpattern) > 0:
            answer = len(newpattern)
    print(answer)
    return answer


solution(s)
