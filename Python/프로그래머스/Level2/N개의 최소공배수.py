arr = [12, 12]


def solution(arr):
    arr = list(set(arr))
    temp = []
    while(True):
        maxn = max(arr)
        flag = False
        for i in range(2, int(maxn)+1):
            flag = False
            for j in range(len(arr)):
                if(arr[j] % i == 0):
                    arr[j] = arr[j]/i
                    flag = True
            if(flag):
                temp.append(i)
                break
        if not flag:
            break

    answer = 1
    for t in temp:
        answer *= t
    print(answer)
    return answer


solution(arr)
