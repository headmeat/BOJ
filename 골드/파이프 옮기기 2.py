from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 1]
dy = [1, 1, 0]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

def dfs(x, y, direction):
    global ans

    if x==n-1 and y==n-1:
        dp[x][y][direction] = 1
        return 1

    for k in range(3):
        if abs(direction-k)>1: continue

        if k==1:
            if not (0<=x+dx[0]<n and 0<=y+dy[0]<n and arr[x+dx[0]][y+dy[0]]==0): continue
            if not (0<=x+dx[2]<n and 0<=y+dy[2]<n and arr[x+dx[2]][y+dy[2]]==0): continue

        if 0<=x+dx[k]<n and 0<=y+dy[k]<n and arr[x+dx[k]][y+dy[k]]==0:
            if visited[x+dx[k]][y+dy[k]][k]==0:
                visited[x+dx[k]][y+dy[k]][k] = 1
                dp[x][y][direction] += dfs(x+dx[k], y+dy[k], k)
            else: dp[x][y][direction] += dp[x+dx[k]][y+dy[k]][k]

    return dp[x][y][direction]

visited = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

visited[0][1][0] = 1
dfs(0, 1, 0)

print(sum(dp[0][1]))
