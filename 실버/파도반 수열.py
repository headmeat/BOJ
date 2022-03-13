from sys import stdin
input = stdin.readline

t = int(input())
dp = [0 for _ in range(101)]
dp[0] = dp[1] = dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i-2] + dp[i-3]

for i in range(t):
    print(dp[int(input())-1])
