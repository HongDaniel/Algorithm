from collections import deque
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]


def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visited = [[0]*col for i in range(row)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == row-1 and y == col-1:  # 도차지에 도달했을 때
            print(visited[x][y])
            return visited[x][y]
        for i in range(4):
            newx, newy = (x+dx[i], y+dy[i])
            if 0 <= newx < row and 0 <= newy < col:
                if visited[newx][newy] == 0 and maps[newx][newy] == 1:
                    visited[newx][newy] = visited[x][y]+1
                    queue.append((newx, newy))
    print(-1)
    return -1


solution(maps)
