from sys import stdin
input = stdin.readline

upper = input().rstrip()
lower = input().rstrip()
n = len(upper)
m = len(lower)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if upper[i-1] == lower[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
ans = ""

while(n!=0 and m!=0):
    if dp[n-1][m] == dp[n][m]:
        n -= 1
    elif dp[n][m-1] == dp[n][m]:
        m -= 1
    else:
        n -= 1
        m -= 1
        ans += upper[n]

print(ans[::-1])
