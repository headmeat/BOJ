from sys import setrecursionlimit
from sys import stdin
input = stdin.readline
setrecursionlimit(10**6)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(i, j):
    if dp[i][j]: return dp[i][j]

    if i==m-1 and j==n-1: return 1
    
    for k in range(4):
        x, y = i+dx[k], j+dy[k]

        if 0<=x<m and 0<=y<n and arr[i][j]>arr[x][y]:
            tmp = solve(x, y)
            dp[i][j] += tmp if tmp>0 else 0

    if dp[i][j] == 0: dp[i][j] = -1
    return dp[i][j]

tmp = solve(0, 0)
print(tmp if tmp>0 else 0)
