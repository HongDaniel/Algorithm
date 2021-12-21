from itertools import combinations as C
from itertools import permutations as P

n = int(input())
stat = []
candi = list(C(list(i for i in range(1, n+1)), n//2))
differ = []


def score(team):  # [1,2,3]
    combi = list(P(team, 2))
    cnt = 0
    for c in combi:
        row = c[0]-1
        col = c[1]-1
        cnt += stat[row][col]
    return cnt


for i in range(n):  # 능력치를 입력받음
    stat.append(list(map(int, input().split())))

for can in candi:  # n의 절반으로 팀을 나누기
    start = [can[i] for i in range(len(can))]
    link = []
    for i in range(1, n+1):  # start에 없는 인원들
        if i not in start:
            link.append(i)
    differ.append(abs(score(start)-score(link)))  # 능력치의 차이를 넣는다

differ.sort()
print(differ[0])
