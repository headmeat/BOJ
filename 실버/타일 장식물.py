from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
dp = [0 for _ in range(81)]
dp[1] = dp[2] = 1

def fibonacci(n):
    if dp[n]:
        return dp[n]

    dp[n] = (fibonacci(n-1) if not dp[n-1] else dp[n-1]) + (fibonacci(n-2) if not dp[n-2] else dp[n-2])

    return dp[n]

fibonacci(n)

print(2*(2*dp[n]+(dp[n-1] if n>1 else 0)))
