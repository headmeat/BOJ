from sys import stdin
input = stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

def solve(n):
    if dp[n]:
        return dp[n]

    sm = 0

    for i in range(n):
        sm += (solve(i) if dp[i] == 0 else dp[i]) * (solve(n-1-i) if dp[n-1-i] == 0 else dp[n-1-i])
    
    dp[n] = sm
    
    return sm

print(solve(n))
