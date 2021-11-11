s = "aabbaccc"


def solution(s):
    answer = 0
    candi = []
    for cutlen in range(1, len(s)//2+1):
        i = 0
        cnt = 0
        pattern = ''
        news = ''
        while (1):
            if i >= len(s):
                break
            cur = s[i:i+cutlen]
            next = s[i+cutlen:i+cutlen+cutlen]
            if cur == next and pattern == cur:
                cnt += 1
                i += cutlen
            elif cur == next and pattern != cur:
                news += str(cnt)+pattern
                pattern = cur
                cnt = 2
                i += cutlen
            else:
                news += cur

        print(news)
    return answer


solution(s)
