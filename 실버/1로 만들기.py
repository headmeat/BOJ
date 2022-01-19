K = int(input())

dp = [-1 for i in range(K+1)]
dp[1] = 0

"""
dp[4] = 2
dp[5] = 3
dp[6] = 2
dp[7] = 3
dp[8] = 3
dp[9] = 2
dp[10] = 3
"""

for i in range(2, K+1):
    if i % 2 == 0:
        if i % 3 == 0: dp[i] = min(dp[i//2] + 1, dp[i//3] + 1)
        else: dp[i] = dp[i//2] + 1
    elif i % 3 == 0: dp[i] = dp[i//3] + 1
    else: dp[i] = dp[i-1] + 1

    dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[K])
