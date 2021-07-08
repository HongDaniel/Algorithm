# input이 1억 이상이면 이분탐색을 의심해보자
n = 6
times = [7, 10]


def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n

    while left <= right:
        middle = (left+right)//2
        people = 0
        for time in times:
            people += middle//time
            if people >= n:
                answer = middle
                right = middle-1
                break
        if people < n:
            left = middle+1

    print(answer)
    return answer


solution(n, times)
