from collections import Counter
color = ["RG", "WR", "BW", "GG"]
prices = [2000, 6000]


def solution(color, prices):
    order = Counter(''.join(color)).most_common()  # 직원들의 주문
    print(order)

    # 같은 색 세트를 주문하고 남은 건 다른 색 세트를 주문
    total1 = 0
    left1 = 0
    for color, num in order:
        total1 += prices[0]*(num//2)
        if num % 2 == 1:
            left1 += 1

    total1 += (left1//2)*prices[1]
    # print(f"total1:{total1}")

    # 같은 색 세트로만 주문
    total2 = 0
    for color, num in order:
        if num % 2 == 0:
            total2 += prices[0]*(num//2)
        else:
            total2 += prices[0]*(num//2+1)
    # print(f"total2:{total2}")

    # 다른 색 세트로만 주문
    total3 = 0
    cnt = 0
    for color, num in order:
        cnt += num
    total3 += prices[1]*(cnt//2)
    # print(f"total3:{total3}")

    return min(total1, total2, total3)


solution(color, prices)
