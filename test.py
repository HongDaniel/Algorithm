a = [[1, -1, 3], [-1, -1, 3]]
for row in a:
    while(1):
        if -1 not in row:
            break
        else:
            row.remove(-1)
            row.append(0)
print(a)
