gold_prices = [2, 5, 1, 3, 4]


def solution(gold_prices):
    answer = -1
    buy_sell = []
    left = 0
    while(1):
        if left >= len(gold_prices)-1:
            break
        right = left+1  # 1
        print(f"left:{left}")
        cnt = 0
        while(1):
            if right == len(gold_prices)-1:
                break
            if gold_prices[left] < gold_prices[right]:
                cnt += 1
            else:
                break
            right += 1
        if cnt > 0:
            buy_sell.append((left, left+cnt))

        left = right

    print(buy_sell)
    return answer


solution(gold_prices)
