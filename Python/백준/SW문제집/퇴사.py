time_profit = []
n = int(input())
dp = [0]*(n+1)
for i in range(n):
    [time, profit] = map(int, input().split())
    time_profit.append([time, profit])

for i in range(n-1, -1, -1):  # 6 5 ... 0
    if time_profit[i][0]+i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], time_profit[i][1] +
                    dp[i+time_profit[i][0]])

print(dp[0])
