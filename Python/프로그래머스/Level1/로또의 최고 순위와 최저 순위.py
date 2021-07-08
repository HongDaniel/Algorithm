lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]


def solution(lottos, win_nums):
    place = {6: "1", 5: "2", 4: "3", 3: "4",
             2: "5", 1: "6", 0: "6"}  # 당첨된 번호 : 순위
    answer = []
    match = 0
    zeros = lottos.count(0)
    for el in lottos:
        if el in win_nums:
            match += 1
    answer.append(int(place[match+zeros]))
    answer.append(int(place[match]))
    print(answer)
    return answer


solution(lottos, win_nums)
