n = int(input())
curves = []
for i in range(n):
    x, y, d, g = map(int, input().split())
    curves.append([x, y, d, g])

dx = [1, 0, -1, 0]  # 0 1 2 3 방향
dy = [0, -1, 0, 1]
visited = [[0] * 101 for i in range(101)]


def get_moves(moves):
    n = len(moves)
    nmoves = list(moves)
    for i in range(n-1, -1, -1):
        tmp = (moves[i]+1) % 4
        nmoves.append(tmp)
    return nmoves


for curve in curves:
    x, y, d, g = curve
    moves = [d]
    visited[x][y] = 1
    for i in range(1, g+1):
        moves = get_moves(moves)
    for m in moves:
        x = x+dx[m]
        y = y+dy[m]
        visited[x][y] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] == 1 and visited[i+1][j] == 1 and visited[i][j+1] == 1 and visited[i+1][j+1] == 1:
            cnt += 1
print(cnt)
