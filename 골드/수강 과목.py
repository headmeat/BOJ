from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if items[i][0]>j: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j-items[i][0]] + items[i][1], dp[i-1][j])

print(dp[n-1][k])
