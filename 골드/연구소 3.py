from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_t = 10**15

def bfs(lst):
    global max_t
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    mt = 0

    for i in range(m):
        v = virus[lst[i]]
        q.append((v[0], v[1], 0))
        visited[v[0]][v[1]] = 0

    while(q):
        x, y, d = q.popleft()
        if arr[x][y]==0: mt = max(mt, d)

        for i in range(4):
            xd, yd = x+dx[i], y+dy[i]
            if 0<=xd<n and 0<=yd<n and arr[xd][yd]!=1 and visited[xd][yd]==-1:
                visited[xd][yd] = d+1
                q.append((xd, yd, d+1))
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=1 and visited[i][j]==-1:
                return
    max_t = min(max_t, mt)
    return

def plot(lst):
    if len(lst)==m:
        bfs(lst)
        return

    for i in range(len(virus)):
        if i in lst: continue
        if len(lst)>0 and lst[-1]>i: continue
        lst.append(i)
        plot(lst)
        del lst[-1]

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            virus.append((i, j))

plot([])

if max_t == 10**15: print(-1)
else: print(max_t)
