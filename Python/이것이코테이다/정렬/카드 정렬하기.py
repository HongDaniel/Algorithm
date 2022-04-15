import heapq
n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, (int(input())))

if len(cards) == 1:
    print(0)
elif len(cards) >= 2:
    answer = 0
    while len(cards) > 1:
        s1 = heapq.heappop(cards)
        s2 = heapq.heappop(cards)
        tmp = s1+s2
        answer += tmp
        heapq.heappush(cards, tmp)
    print(answer)
