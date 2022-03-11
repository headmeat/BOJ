from sys import stdin
from collections import deque
input = stdin.readline

def solve(i, arr):
    c = 0

    if i == n-1: 
        if len(arr): return m - arr[-1] - 1
        else: dp[i] = [1 for _ in range(m)]

    for j in range(m-n+i+1):
        if len(arr) and j<=arr[-1]: continue

        if dp[i][j]: c += dp[i][j]
        else:
            arr.append(j)
            dp[i][j] += solve(i+1, arr)
            c += dp[i][j]
            del arr[-1]

    return c

test_case = int(input())

for t in range(test_case):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]

    solve(0, [])

    print(sum(dp[0]))
