T = int(input())

N = [int(input()) for i in range(T)]

mx = max(N)

dp = [[0,0] for i in range(mx+1)]
#0횟수, 1횟수
dp[0] = [1, 0]
if mx >= 1: dp[1] = [0, 1]

for i in range(2, mx+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in N:
    print(" ".join(map(str, dp[i])))
