n = 15


def solution(n):
    answer = 0

    for i in range(1, int((n+1)/2)):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if(temp == n):
                answer += 1
                break
            elif(temp > n):
                break

    print(answer+1)
    return answer+1


solution(n)
