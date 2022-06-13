from sys import stdin
input = stdin.readline

arr = list(map(int, input().split()))

visited = [[0 for _ in range(40)] for _ in range(40)]
#동서남북
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0

def dfs(x, y, count, p):
    global ans, dx, dy, visited

    if count==arr[0]:
        ans += p
        return
    
    for k in range(4):
        if arr[k+1]==0 or visited[x+dx[k]][y+dy[k]]: continue

        visited[x+dx[k]][y+dy[k]] = 1
        dfs(x+dx[k], y+dy[k], count+1, p*(arr[k+1]/100))
        visited[x+dx[k]][y+dy[k]] = 0

visited[20][20] = 1
dfs(20, 20, 0, 1)

print(ans)
