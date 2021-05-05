# 다익스트라 알고리즘을 활용한 풀이
import heapq
N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3


def solution(N, road, K):
    dist = [float('inf')]*(N+1)
    dist[1] = 0
    heap = []
    answer = 0
    heapq.heappush(heap, [1, 0])
    while len(heap) > 0:
        current_node, current_cost = heapq.heappop(heap)
        for srt, dest, cost in road:
            next_cost = current_cost+cost
            if current_node == srt and next_cost < dist[dest]:
                dist[dest] = next_cost
                heapq.heappush(heap, [dest, next_cost])
            if current_node == dest and next_cost < dist[srt]:
                dist[srt] = next_cost
                heapq.heappush(heap, [srt, next_cost])
    # print(dist)
    for dis in dist:
        if dis <= K:
            answer += 1
    return answer


solution(N, road, K)
