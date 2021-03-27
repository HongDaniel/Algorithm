ar = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 1]

for i in range(len(ar)):
    min_index = i  # 최소값의 인덱스
    for j in range(i+1, len(ar)):
        if(ar[j] < ar[min_index]):
            min_index = j
    ar[i], ar[min_index] = ar[min_index], ar[i]

print(ar)
