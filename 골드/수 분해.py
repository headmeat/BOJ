from sys import stdin
input = stdin.readline

n=int(input())
dp=[0 for _ in range(1000001)]

for i in range(4):
    dp[i] = i

for i in range(4, n+1):
    dp[i] = max(dp[i-2]*2, dp[i-3]*3)

print(dp[n]%10007)
