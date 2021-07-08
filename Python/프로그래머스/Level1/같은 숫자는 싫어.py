arr = [4, 4, 4, 3, 3]


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if(arr[i] == arr[i-1]):  # 전 원소와 같으면 스킵
            continue
        else:
            answer.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    return answer


print(solution(arr))
