prices = [1, 2, 3, 2, 3]


def solution(prices):
    answer = [0]*len(prices)

    for i in range(len(prices)):
        start = 0
        for j in range(i+1, len(prices)):
            start += 1
            if(prices[i] > prices[j]):
                break
        answer[i] = start
    # print(answer)
    return answer


solution(prices)
