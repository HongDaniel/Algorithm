dx = [0, -1, -1, -1, 0, 1, 1, 1]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cx = [-1, -1, 1, 1]  # ↖, ↗, ↘, ↙
cy = [-1, 1, 1, -1]
water = []
direction = []


def getinfo():
    for i in range(n):  # 물바구니 정보 저장
        ar = list(map(int, input().split()))
        water.append(ar)
    for j in range(m):
        a, b = map(int, input().split())
        direction.append([a, b])


# 정보 입력
n, m = map(int, input().split())
getinfo()


def moveCloud(i, s, cloud):
    newCloud = []
    for dot in cloud:  # [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
        x, y = dot[0], dot[1]
        # print(f"x, y:{x}, {y}")
        # print(f"dx:{dx[i]} dy:{dy[i]}")
        # if 0 <= x+dx[i]*s < n:
        #     x = x+dx[i]*s
        # elif x+dx[i]*s < 0:
        #     x = n-1
        # else:
        #     x = 0
        # if 0 <= y+dy[i]*s < n:
        #     y = y+dy[i]*s
        # elif y+dy[i]*s < 0:
        #     y = n-1
        # else:
        #     y = 0
        nx = (n+x+dx[i]*s) % n
        ny = (n+y+dy[i]*s) % n
        newCloud.append([nx, ny])
    return newCloud


def rain(cloud):
    for dot in cloud:
        x, y = dot[0], dot[1]
        water[x][y] += 1


def watercopy(cloud):
    for dot in cloud:
        x, y = dot[0], dot[1]
        cnt = 0
        for i in range(4):
            if 0 <= x+cx[i] < n and 0 <= y+cy[i] < n:
                if water[x+cx[i]][y+cy[i]] > 0:
                    cnt += 1
        water[x][y] += cnt


def newCloud(cloud):
    tmp = []
    for row in range(n):
        for col in range(n):
            if water[row][col] >= 2 and [row, col] not in cloud:
                tmp.append([row, col])
    # tmp.sort()  # 보기 좋게 정렬
    # print(f"tmp:{tmp}")
    for (row, col) in tmp:  # 구름이 생기면 물이 2감소
        water[row][col] -= 2
    return tmp


cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]  # 첫번째 구름

for d in direction:
    movedcloud = moveCloud(d[0]-1, d[1], cloud)  # i번째 방향으로 s만큼 움직임
    rain(movedcloud)  # 비가 내림
    watercopy(movedcloud)  # 물복사시전
    cloud = newCloud(movedcloud)  # 새로운 구름생성
    # print(f"new cloud:{cloud}")
    # print(f"water:{water}")
answer = 0
for row in water:
    answer += sum(row)
print(answer)
