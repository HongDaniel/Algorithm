n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
for el in b:
    s, e = 0, len(a)-1
    flag = False
    while(s <= e):
        mid = (s+e)//2
        if el == a[mid]:
            flag = True
            break
        if el > a[mid]:
            s = mid+1
        elif el < a[mid]:
            e = mid-1

    if flag:
        print(1)
    else:
        print(0)
