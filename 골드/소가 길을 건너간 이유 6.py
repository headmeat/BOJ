from sys import stdin
from collections import deque
input = stdin.readline

n,k,r = map(int, input().split())
roads = [[[] for _ in range(n)] for _ in range(n)]
farm = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []

def bfs(x, y):
    global visited, roads
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    cows = farm[x][y]

    while(q):
        a, b = q.popleft()

        for k in range(4):
            if 0<=a+dx[k]<n and 0<=b+dy[k]<n and visited[a+dx[k]][b+dy[k]]==0 and [a+dx[k], b+dy[k]] not in roads[a][b]:
                visited[a+dx[k]][b+dy[k]] = 1
                q.append((a+dx[k], b+dy[k]))
                cows += farm[a+dx[k]][b+dy[k]]

    return cows

for i in range(r):
    a,b,c,d = map(int, input().split())
    roads[a-1][b-1].append([c-1, d-1])
    roads[c-1][d-1].append([a-1, b-1])

for i in range(k):
    a,b = map(int, input().split())
    farm[a-1][b-1] += 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0: 
            cows = bfs(i, j)
            if cows>0: ans.append(cows)

res = 0

for i in range(len(ans)):
    tmp = ans[i]

    for j in range(i+1, len(ans)):
        res += tmp * ans[j]

print(res)
