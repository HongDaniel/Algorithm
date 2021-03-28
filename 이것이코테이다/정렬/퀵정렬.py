ar = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quicksort(ar, start, end):
    if start >= end:  # 원소가 한 개일 때
        return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and ar[pivot] >= ar[left]:
            left += 1

        while right > start and ar[pivot] <= ar[right]:
            right -= 1

        if left > right:
            ar[pivot], ar[right] = ar[right], ar[pivot]

        else:
            ar[left], ar[right] = ar[right], ar[left]

    quicksort(ar, start, right-1)
    quicksort(ar, right+1, end)


quicksort(ar, 0, len(ar)-1)
print(ar)
