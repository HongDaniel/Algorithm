n, m, k = map(int, input().split())  # n: 배열의 크기 m: 더하는 횟 수 k: 연속 횟수
array = list(map(int, input().split()))

array.sort()
answer = 0
kcount = 0
print(array[-1])
print(array[-2])

for i in range(m):
    if(kcount < k):
        answer += array[-1]
        kcount += 1
    else:
        answer += array[-2]
        kcount = 0

print(answer)
