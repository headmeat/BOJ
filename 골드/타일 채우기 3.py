from sys import stdin
input = stdin.readline

n = int(input())

dp = [[0 for _ in range(2)] for _ in range(1000001)]
dp[0][0] = 0
dp[1][0] = 2
dp[2][0] = 7
dp[2][1] = 1

for i in range(3, n+1):
    dp[i][1] = dp[i-1][1] + dp[i-3][0]
    dp[i][0] = (dp[i-1][0]*2 + dp[i-2][0]*3 + dp[i][1]*2)%1000000007

print(dp[n][0])
