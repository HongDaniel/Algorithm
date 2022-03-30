estimates = [1, 1, 10, 10, 10, 10, 10, 10]
k = 6


def solution(estimates, k):
    answer = 0
    left = 0
    right = k-1
    partial_sum = sum(estimates[left:left+k])
    answer = sum(estimates[left:left+k])
    print(partial_sum)
    while(1):
        partial_sum -= estimates[left]
        left += 1
        right += 1
        if right == len(estimates):
            break
        partial_sum += estimates[right]
        print(f"left:{left} right:{right}")
        if answer < partial_sum:
            answer = partial_sum

    print(answer)
    return answer


solution(estimates, k)
