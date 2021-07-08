t = [0, 1, 2, 0]
r = [0, 1, 2, 3]


def solution(t, r):
    answer = []
    order = 0
    infos = [[]for i in range(len(r))]  # 승객이름 도착시간 등급

    for i, j in zip(t, r):
        infos[order].append(order)
        infos[order].append(i)
        infos[order].append(j)
        order += 1
    infos.sort(key=lambda x: x[2])  # 등급에 따라 정렬
    infos.sort(key=lambda x: x[1])  # 도착시간에 따라 정렬
    waitlist = []

    for i in range(max(t)+1):  # 리프트
        count = 0
        temp = []
        for info in infos:
            if info[1] == i:
                count += 1
                temp.append(info)
        print(f"{i} 번째 count:{count} ")

        if count > 1:
            answer.append(temp[0][0])
            for info in temp[1:]:
                waitlist.append(info)
        else:
            if len(waitlist) == 0:  # 아무도 안기다릴때
                if temp:
                    answer.append(temp[0][0])
            else:  # 기다리는 사람이 있을 때
                if temp:
                    if waitlist[0][2] > temp[0][2]:
                        answer.append(temp[0][0])
                    else:
                        answer.append(waitlist[0][0])

                else:
                    answer.append(waitlist[0][0])
                    waitlist.pop(0)

        print(f"waitlist:{waitlist}")
        print(f"temp:{temp}")
        print(f"answer:{answer}")

    # print(infos)
    print(answer)
    return answer


solution(t, r)
