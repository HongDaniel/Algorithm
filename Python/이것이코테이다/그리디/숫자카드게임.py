row, col = map(int, input().split())

array = [list(map(int, input().split())) for i in range(row)]
temp = []
for i in range(row):
    temp.append(min(array[i]))

print(max(temp))
