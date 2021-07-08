strings = ['sun', 'bed', 'car']
n = 1

###############################
# 중요개념!
a = {'a': 50, 'c': 10, 'b': 20}

sorted1 = sorted(a.items(), key=lambda x: x[1])
print(sorted1)
###############################


def solution(strings, n):
    answer = []
    arr = {}  # 딕셔너리 정의
    strings.sort()  # 오름차순 정렬
    for i in range(len(strings)):
        arr[strings[i]] = (strings[i][n])  # n번째 요소
    sorted_arr = dict(sorted(arr.items(), key=lambda x: x[1]))
    for i in sorted_arr.keys():
        answer.append(i)
    return answer


print(solution(strings, n))
