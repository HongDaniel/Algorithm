n, m = map(int, input().split())  # 맵의 크기
x, y, direction = list(map(int, input().split()))  # 시작 지점
ar = [list(map(int, input().split())) for i in range(n)]
# print(ar)

visited = [[0]*m for i in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(visited)


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


answer = 1
turn_time = 0
visited[x][y] = 1

while(1):
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    if visited[nx][ny] == 0 and ar[nx][ny] == 0:  # 가보지 않은 항
        x = nx
        y = ny
        answer += 1
        visited[x][y] = 1
        turn_time = 0
        continue
    else:  # 바다이거나 가본 곳
        turn_time += 1

    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        if ar[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            turn_time = 0

print(answer)
