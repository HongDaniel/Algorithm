from collections import defaultdict
money = 4578
costs = [1, 4, 99, 35, 50, 1000]


def minCost(value_cost, money):
    dp = [0]*(money+1)  # 1원만 사용했을 때

    for value in value_cost.keys():
        for i in range


def solution(money, costs):
    answer = 0
    value_cost = {}
    for i in range(len(costs)):
        if i == 0:
            value_cost[1] = costs[i]
        elif i == 1:
            value_cost[5] = costs[i]
        elif i == 2:
            value_cost[10] = costs[i]
        elif i == 3:
            value_cost[50] = costs[i]
        elif i == 4:
            value_cost[100] = costs[i]
        elif i == 5:
            value_cost[500] = costs[i]
    # print(value_cost)
    answer = minCost(value_cost, money)
    return answer


solution(money, costs)
