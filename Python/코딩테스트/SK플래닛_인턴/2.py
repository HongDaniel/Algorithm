deposit = [500, 1000, -300, 200, -200, 100, -100]


def solution(deposit):
    answer = []
    for el in deposit:
        if el > 0:  # 입금
            answer.append(el)

        else:  # 출금
            takeout = 0  # 통장에서 출금하는 금액
            while(1):  # 출금하는 금액을 맞춤
                takeout += answer.pop()
                if takeout >= -el:
                    takeout += el
                    break
            if takeout:  # 0원 초과일 때만 다시 입금
                answer.append(takeout)
        print(answer)
    return answer


solution(deposit)
