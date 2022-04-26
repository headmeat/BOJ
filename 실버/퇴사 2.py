from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
mx = 0

for i in range(n):
    t, p = arr[i]

    dp[i] = max(mx, dp[i])
    mx = dp[i]
    if i+t<=n: dp[i+t] = max(dp[i+t], p+dp[i])

print(max(mx, dp[-1]))
