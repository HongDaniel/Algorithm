for h in range(height):
    for row in range(len(graph[h])):
        if 0 in graph[h][row]:
            answer = -1
            break
        if answer < max(graph[h][row]):
            answer = max(graph[h][row])