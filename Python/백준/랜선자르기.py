k, n = map(int, input().split())
wires = []
for i in range(k):
    wires.append(int(input()))
start = 1
end = max(wires)
answer = 0
while(start <= end):
    mid = (start+end)//2
    cnt = 0
    for wire in wires:
        cnt += wire//mid
    if cnt >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
