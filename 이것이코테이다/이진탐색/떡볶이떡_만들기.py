# 조사해야하는 값이 1억 이상이면 이진탐색으로 값을 찾자

n, target = map(int, input().split())
ar = list(map(int, input().split()))

ar.sort()

start = 0
end = max(ar)

while start < end:
    mid = (start+end)//2
    temp = 0
    for i in range(len(ar)):
        if mid < ar[i]:
            temp += ar[i]-mid

    if temp == target:
        print(mid)
        break

    elif temp < target:
        end = mid-1

    else:
        start = mid+1
