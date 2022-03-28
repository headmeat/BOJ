from sys import stdin
input = stdin.readline

n = int(input())

dp = [0 for _ in range(91)]

dp[1] = dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
