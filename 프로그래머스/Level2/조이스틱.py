name = "JEROEN"


def solution(name):
    name = list(name)
    answer = 0
    index = 0

    while(1):
        # 원하는 알파벳으로 이동
        answer += min(ord(name[index])-ord('A'), ord('Z')-ord(name[index])+1)
        name[index] = 'A'

        if name.count('A') == len(name):
            print(answer)
            return answer

        # 왼쪽으로 갈 건지 오른쪽으로 갈 건지 결정
        left, right = (1, 1)
        for l in range(1, len(name)):
            if name[index-l] == 'A':
                left += 1
            else:
                break
        for r in range(1, len(name)):
            if name[index+r] == 'A':
                right += 1
            else:
                break

        if left >= right:
            index += right
            answer += right
        else:
            index -= left
            answer += left


solution(name)
