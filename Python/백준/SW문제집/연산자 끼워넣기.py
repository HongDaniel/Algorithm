# 재귀함수를 할용한 풀이

max_v = -987654321
min_v = 987654321
N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

cnt = 1


def dfs(cnt, result, add, sub, mul, div):
    global max_v
    global min_v
    if cnt == N:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return
    if add > 0:
        dfs(cnt+1, result+num[cnt], add-1, sub, mul, div)
    if sub > 0:
        dfs(cnt+1, result-num[cnt], add, sub-1, mul, div)
    if mul > 0:
        dfs(cnt+1, result*num[cnt], add, sub, mul-1, div)
    if div > 0:
        if result < 0:
            result = -(-(result)//num[cnt])
        else:
            result = result//num[cnt]
        dfs(cnt+1, result, add, sub, mul, div-1)


dfs(cnt, num[0], add, sub, mul, div)
print(max_v)
print(min_v)
