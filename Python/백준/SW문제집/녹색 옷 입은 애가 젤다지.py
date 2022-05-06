# 우선순위 큐를 이용한 풀이
import heapq
board = [
    [5, 5, 4],
    [3, 9, 1],
    [3, 2, 7]]
INF = 987654321
n = len(board)


def bfs(board):
    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    min_dis = [[INF]*n for i in range(n)]
    visited = [[False]*n for i in range(n)]
    min_dis[0][0] = board[0][0]  # 시작점
    hq = []
    heapq.heappush(hq, [board[0][0], 0, 0])
    while hq:
        cost, x, y = heapq.heappop(hq)
        visited[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if cost+board[nx][ny] < min_dis[nx][ny]:
                    min_dis[nx][ny] = min(cost+board[nx][ny], min_dis[nx][ny])
                    heapq.heappush(hq, [min_dis[nx][ny], nx, ny])
    return min_dis[n-1][n-1]


seq = 0
answer = []
while(1):
    n = int(input())
    if(n == 0):
        break
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    answer.append(bfs(board))
    # print(f"Problem {seq}: {answer}")
for i in range(len(answer)):
    seq = i+1
    print(f"Problem {seq}: {answer[i]}")
