from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def surround(v):
    global ans
    smallest_wall = 100
    water = 0

    for i in range(n):
        for j in range(m):
            if v[i][j]==1:
                for k in range(4):
                    if 0<=i+dx[k]<n and 0<=j+dy[k]<m: 
                        if v[i+dx[k]][j+dy[k]]==0: smallest_wall = min(smallest_wall, arr[i+dx[k]][j+dy[k]])
                        continue
                    else: return

    for i in range(n):
        for j in range(m):
            if v[i][j]==1:
                total_visited[i][j] = 1
                water += smallest_wall - arr[i][j]
                arr[i][j] += smallest_wall - arr[i][j]

    ans += water

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    mx = arr[x][y]

    while(q):
        a, b = q.popleft()

        for k in range(4):
            if 0<=a+dx[k]<n and 0<=b+dy[k]<m and visited[a+dx[k]][b+dy[k]]==0 and mx>=arr[a+dx[k]][b+dy[k]]:
                visited[a+dx[k]][b+dy[k]] = 1
                q.append((a+dx[k], b+dy[k]))

    surround(visited)

total_visited=[[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if total_visited[i][j]==0:
            bfs(i, j)

print(ans)
