from itertools import combinations
from collections import Counter
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        flag = True
        for order in orders:  # order에 대한 조합을 구하기
            for result in combinations(sorted(order), c):
                temp.append(result)
        temp = Counter(temp).most_common()
        if temp:
            maximum = temp[0][1]
            if maximum > 1:  # 1명 이상의 손님으로부터 주문된 것만
                for el in temp:
                    if el[1] == maximum:
                        answer.append("".join(el[0]))
    answer = sorted(answer)
    print(answer)
    return answer


solution(orders, course)
