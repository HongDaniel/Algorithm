n = int(input())
curves = []
for i in range(n):
    x, y, d, g = map(int, input().split())
    curves.append([x, y, d, g])
print(curves)