n = int(input())
schedule = []
for i in range(n):
    schedule.append(list(map(int, input().split())))
schedule.sort(key=lambda x: x[0])
schedule.sort(key=lambda x: x[1])
meeting = [schedule[0]]
idx = 1

while(1):
    start, end = meeting[-1]
    if idx >= len(schedule):
        break
    if schedule[idx][0] >= end:
        meeting.append(schedule[idx])
    idx += 1

print(len(meeting))
