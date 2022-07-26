from sys import stdin
input = stdin.readline

n = int(input())

dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3
dp[4] = 11

for i in range(6, n+1, 2):
    dp[i] += dp[i-2]*dp[2] + sum([dp[x] * 2 for x in range(i-4, -1, -2)])

print(dp[n])
