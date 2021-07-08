n = int(input())
ar = list(map(int, input().split()))
print(ar)

d = [0]*101

d[0] = ar[0]
d[1] = ar[1]
for i in range(2, len(ar)):
    d[i] = max(d[i-2]+ar[i], d[i-1])

print(d[len(ar)-1])
