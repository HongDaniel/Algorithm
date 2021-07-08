n, m = map(int, input().split())  # n: 화폐의 종류 m: 만들고자하는 수
ar = []

for i in range(n):
    ar.append(int(input()))
# print(ar)

ar.sort()

d = [10001]*(m+1)
d[0] = 0

for i in range(n):  # 화폐의 종류
    for j in range(ar[i], m+1):  # 화폐단위 ~ 만들고자 하는 값
        if d[j-ar[i]] != 10001:
            d[j] = min(d[j-ar[i]]+1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
