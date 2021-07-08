msg = 'KAKAO'


def solution(msg):
    answer = []
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]  # 알파벳 나열하기
    dic = {}
    for i, el in enumerate(alpha):  # 사전 초기화
        dic[el] = i+1

    index = 0
    length = 0
    last = 27

    while index < len(msg):
        # print(f"index: {index}")
        length += 1
        # print(msg[index:index+length])
        if msg[index:index+length] in dic.keys():  # 사전에 있을 경우
            if index+length == len(msg):
                answer.append(dic[msg[index:index+length]])
                break

        else:  # 사전에 없을 경우
            answer.append(dic[msg[index:index+length-1]])
            dic[msg[index:index+length]] = last
            last += 1
            index += length-1
            length = 0
    print(answer)
    return answer


solution(msg)
