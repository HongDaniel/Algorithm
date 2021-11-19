msg = 'TOBEORNOTTOBEORTOBEORNOT'


def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):
        dic[chr(64+i)] = i

    start = 0
    end = 1
    while(1):
        curWord = msg[start:end]  # 검색하는 문자열
        lastWord = msg[start:end-1]  # 전 문자열
        # print(f"curWord: {curWord}")
        if curWord in dic.keys():  # 검색하는 문자가 사전에 있을 경우
            end += 1

        else:  # 없을 경우
            answer.append(dic[lastWord])
            dic[curWord] = len(dic)+1
            start = end-1  # 1
            end = start+1  # 2
        if start == len(msg)-1 or end == len(msg)+1:
            answer.append(dic[msg[start:end]])
            break

    print(answer)
    return answer


solution(msg)
