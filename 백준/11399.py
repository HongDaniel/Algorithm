n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 0
for i in a:
    result += i*n
    n -= 1
    if n == 0:
        break
print(result)
#핵심 : n = list(map(int,input().split()))
