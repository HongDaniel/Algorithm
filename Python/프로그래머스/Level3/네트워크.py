n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def bfs(start, computers, visited):
    q = [start]
    visited[start] = 1
    while(q):
        top = q.pop(0)
        visited[top] = 1
        for idx, node in enumerate(computers[top]):
            if node == 1 and visited[idx] == 0:
                q.append(idx)


def solution(n, computers):
    answer = 0
    visited = [0]*n
    for idx, com in enumerate(computers):
        if visited[idx] == 0:
            bfs(idx, computers, visited)
            answer += 1
    print(answer)
    return answer


solution(n, computers)
