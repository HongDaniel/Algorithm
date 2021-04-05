from itertools import combinations
from collections import Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]


def solution(orders, course):
    tem = []
    orders = orders
    # orders를 알파벳 순으로 정렬
    for el in orders:
        tem.append("".join(sorted(list(el))))
    orders = tem
    # print(orders)
    answer = []

    for num in course:
        temp = []
        flag = True
        for order in orders:
            if num > len(order):
                flag = False
                print(f"num:{num} order:{order}")
            else:
                for i in combinations(order, num):
                    temp.append(i)
                flag = True
        if flag:
            temp = Counter(temp)
            most = temp.most_common()
            modes = []
            maxium = most[0][1]
            if maxium > 1:  # 최소 2명
                for num in most:
                    if num[1] == maxium:
                        modes.append(''.join(num[0]))
                for el in modes:
                    answer.append(el)
    answer = sorted(answer)
    print(answer)
    return answer


solution(orders, course)
