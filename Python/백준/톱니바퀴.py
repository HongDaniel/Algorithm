wheels = []
for i in range(4):
    wheels.append(list(map(int, input())))
k = int(input())
turns = []
for i in range(k):
    turns.append(list(map(int, input().split())))


def clock_wise(ar):  # 시계방향으로 회전
    tmp = list(ar)
    right = tmp.pop()
    tmp.insert(0, right)
    return tmp


def counter_wise(ar):  # 반시계방향으로 회전
    tmp = list(ar)
    left = tmp.pop(0)
    tmp.append(left)
    return tmp


def get_score(wheels):
    tmp_score = 0
    for i in range(len(wheels)):
        tmp_score += wheels[i][0] * (2**i)
    return tmp_score


for turn in turns:
    n, d = turn[0]-1, turn[1]
    should_turn = [(n, d)]
    left = wheels[n][-2]  # n번째 바퀴의 왼쪽
    right = wheels[n][2]  # n번째 바퀴의 오른쪽
    left_dir, right_dir = d, d
    for i in range(n-1, -1, -1):
        if wheels[i][2] != left:  # 좌 4와 우 0이 같은지
            left_dir = left_dir*(-1)
            should_turn.append((i, left_dir))
        else:
            break
        left = wheels[i][-2]

    for i in range(n+1, 4):
        if wheels[i][-2] != right:  # 좌 4와 우 0이 같은지
            right_dir = right_dir*(-1)
            should_turn.append((i, right_dir))
        else:
            break
        right = wheels[i][2]

    for turn in should_turn:  # 실제로 회전
        n, d = turn
        if d == 1:  # 시계방향
            wheels[n] = clock_wise(wheels[n])
        else:  # 반시계방향
            wheels[n] = counter_wise(wheels[n])

score = get_score(wheels)
print(score)
