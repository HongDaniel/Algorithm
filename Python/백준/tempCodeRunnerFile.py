m, n = map(int, input().split())
nodes = []
for i in range(n):
    nodes.append(list(map(int, input().split())))
board = [[] for i in range(m+1)]
visited = [0]*(m+1)


def bfs(board, m):
    q = []
    cnt = 0
    for idx in range(1, m+1):
        if not visited[idx]:
            visited[idx] = 1
            q.append(idx)
            cnt += 1
            while q:
                top = q.pop(0)
                print(top)
                for n in board[top]:

                    if visited[n] == 0:
                        # print(n)
                        visited[n] = 1
                        q.append(n)
    return cnt


def solution():
    for node in nodes:
        board[node[0]].append(node[1])
        board[node[1]].append(node[0])
    answer = bfs(board, m)
    print(board)
    print(answer)
    return answer


solution()
