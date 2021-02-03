ar = []
a, b, c = map(int, input().split())
ar.append(a)
ar.append(b)
ar.append(c)
ar.sort()
for i in range(len(ar)):
    print(ar[i], end=" ")
