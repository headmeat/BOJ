from sys import stdin
input = stdin.readline

n=int(input())
dp = [0 for _ in range(10**6+1)]

for i in range(2, n+1):
    m = 10**6+1
    if i%2==0: m = min(m, dp[i//2])
    if i%3==0: m = min(m, dp[i//3])
    m = min(m, dp[i-1])

    dp[i] = m+1

print(dp[n])
