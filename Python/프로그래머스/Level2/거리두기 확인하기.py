def check(x, y, place, visited, cnt):
    visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # print((x,y))
    if cnt == 2:
        return True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
            if place[nx][ny] == 'P':
                # print('Nope!')
                return False
            elif place[nx][ny] == 'O':
                if check(nx, ny, place, visited, cnt+1) == False:
                    return False
            else:
                continue


def solution(places):
    answer = []
    for place in places:
        flag = True
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    visited = [[0]*5 for i in range(5)]
                    cnt = 0
                    if check(row, col, place, visited, cnt) == False:
                        flag = False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    print(answer)

    return answer
