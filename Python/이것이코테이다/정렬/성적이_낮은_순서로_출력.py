n = int(input())
ar = {}  # 학생:점수
for i in range(n):
    temp = []
    temp.append(input().split())
    ar[temp[0][0]] = int(temp[0][1])

ar1 = sorted(ar.items())  # 리스트 형태 반환
for i in range(n):
    print(ar1[i][0], end=" ")
