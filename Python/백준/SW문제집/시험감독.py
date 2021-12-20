import math
places = int(input())
participants = list(map(int, input().split()))
top, sub = map(int, input().split())
answer = 0

for p in participants:
    p = p-top
    answer += 1
    if(p >= 0):
        answer += math.ceil(p/sub)

print(answer)
