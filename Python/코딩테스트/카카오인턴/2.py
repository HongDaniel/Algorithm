from itertools import combinations as com
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def distance(l1, l2):
    return abs(l1[0]-l2[0])+abs(l1[1]-l2[1])


def solution(places):
    answer = []
    for place in places:
        print(place)
        plocation = []
        candidates = []
        for i in range(len(place)):  # P 위치
            place[i] = list(place[i])
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    plocation.append((i, j))
        # print(plocation)
        flag2 = True
        for i, j in com(plocation, 2):  # 거리가 2이하인 참가자들
            if distance(i, j) <= 2:
                candidates.append((i, j))
                if distance(i, j) == 1:
                    flag2 = False

        if not flag2:
            answer.append(0)
            # print('case1')
            continue

        if len(candidates) == 0:
            answer.append(1)
            # print('case2')
            continue

        else:
            flag = True
            for p in candidates:
                x1, y1, x2, y2 = (p[0][0], p[0][1], p[1][0], p[1][1])
                if y1-y2 == 2 and place[x1][y1-1] == 'O':
                    flag = False
                elif y2-y1 == 2 and place[x1][y1+1] == 'O':
                    flag = False
                elif x1-x2 == 2 and place[x1-1][y1] == 'O':
                    flag = False
                elif x2-x1 == 2 and place[x1+1][y1] == 'O':
                    flag = False
                elif (y1-y2 == 1 and x1-x2 == 1 and place[x1][y1-1] == 'O') or (y1-y2 == 1 and x1-x2 == 1 and place[x1-1][y1] == 'O'):
                    flag = False
                elif (y1-y2 == -1 and x1-x2 == 1 and place[x1][y1+1] == 'O') or (y1-y2 == -1 and x1-x2 == 1 and place[x1-1][y1] == 'O'):
                    flag = False
                elif (y1-y2 == 1 and x1-x2 == -1 and place[x1][y1-1] == 'O') or (y1-y2 == 1 and x1-x2 == -1 and place[x1+1][y1] == 'O'):
                    flag = False
                elif (y1-y2 == -1 and x1-x2 == -1 and place[x1][y1+1] == 'O') or (y1-y2 == -1 and x1-x2 == -1 and place[x1+1][y1] == 'O'):
                    flag = False
            if flag:
                answer.append(1)
                # print('case3')
                continue
            else:
                answer.append(0)
                # print('case4')
                continue
    print(answer)
    return answer


solution(places)
