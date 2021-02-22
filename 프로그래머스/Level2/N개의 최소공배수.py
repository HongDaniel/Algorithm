arr = [12, 12, 10]


def solution(arr):
    arr = list(set(arr))
    maxn = max(arr)
    temp = []

    for i in range(1, maxn+1):
        flag = False
        for j in range(len(arr)):
            if(arr[j] % i == 0):
                arr[j] /= i
                flag = True
        if(flag):
            temp.append(i)

    print(f"arr:{arr}")
    answer = 1
    temp.extend(arr[0:])
    print(f"temp:{temp}")
    for i in temp:
        answer *= i
    print(int(answer))
    return int(answer)


solution(arr)
