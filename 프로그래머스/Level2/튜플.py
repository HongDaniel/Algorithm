import re

s = "{{20,111},{111}}"


def solution(s):
    answer = []
    s = s[2:-2]  # 문자열 슬라이싱
    s = s.split('},{')  # 리스트 형태로 반환
    s.sort(key=len)  # 문자열도 이런식으로 정렬이 가능

    for string in s:
        ar = string.split(',')
        print(ar)
        for el in ar:
            if int(el) not in answer:
                answer.append(int(el))
    print(answer)


solution(s)
