# n, k = map(int, input().split())
# belt = list(map(int, input().split()))
# print(belt)
from collections import deque
n, k = 3, 2
belt = deque([1, 2, 1, 2, 1, 2])
robot = deque([0]*n)
cnt = 0

while(1):
    belt.rotate(1)
    robot.rotate(1)
    if robot[0] != 0:
        robot.popleft()
        robot.appendleft(0)

    if belt.count(0) >= k:
        break
