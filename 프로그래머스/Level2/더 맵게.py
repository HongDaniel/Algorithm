import heapq

scoville = [2, 3]
K = 7


def solution(scoville, K):
    answer = 0
    heap = heapq.heapify(scoville)

    while (len(heap) >= 2):
        a = heapq.heappop(heap)
        if(a >= K):
            print(answer)
            return answer
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer += 1

        # 원소가 1개 남았을 때
        if(len(heap) == 1 and heap[-1] < K):
            return -1

        elif(len(heap) == 1 and heap[-1] >= K):
            return answer
    print(answer)


solution(scoville, K)
