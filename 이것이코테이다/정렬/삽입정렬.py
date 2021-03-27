ar = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 1]


for i in range(1, len(ar)):
    for j in range(i, 0, -1):
        if ar[j] < ar[j-1]:
            ar[j], ar[j-1] = ar[j-1], ar[j]
        else:
            break


print(ar)
