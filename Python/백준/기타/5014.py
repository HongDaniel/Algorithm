# from collections import deque
from collections import defaultdict
# F, S, G, U, D = 100, 2, 1, 1, 0  # F:총 층수 S: 현재층수 G:도착위치
F, S, G, U, D = map(int, input().split(" "))
answer = 0
visited = [0]*(F+1)
q = [S]
flag = True
while(q):
    if G in q:
        print(answer)
        flag = False
    cur = q.pop(0)
    up = cur+U
    down = cur-D
    if 1 <= up <= F and visited[up] == 1 and 1 <= down <= F and visited[down] == 1:
        continue
    if 1 <= up <= F and up not in visited:
        q.append(up)
        visited[up] = 1
    if 1 <= down <= F and down not in visited:
        q.append(down)
        visited[down] = 1
    answer += 1
    # print(f"q:{q}")
    # print(f"visited:{visited}")
    # print(f"answer:{answer}")
    # print()
if flag:
    print("use the stairs")
