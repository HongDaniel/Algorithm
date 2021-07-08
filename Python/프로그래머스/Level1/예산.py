d = [2, 2, 3, 3]
budget = 10


def solution(d, budget):
    answer = 0
    d.sort()
    for price in d:
        if price > budget:
            break
        budget -= price
        answer += 1
    print(answer)
    return answer


solution(d, budget)
