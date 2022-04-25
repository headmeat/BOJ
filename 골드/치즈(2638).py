from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
melt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    q.append((x, y))
    stack = []

    while(q):
        a, b = q.popleft()

        for k in range(4):
            if 0>a+dx[k] or a+dx[k]>=n or 0>b+dy[k] or b+dy[k]>=m: continue

            if arr[a+dx[k]][b+dy[k]]:
                visited[a+dx[k]][b+dy[k]] += 1
                if visited[a+dx[k]][b+dy[k]]>=2: stack.append((a+dx[k], b+dy[k]))
            elif visited[a+dx[k]][b+dy[k]]==0:
                visited[a+dx[k]][b+dy[k]] = 1
                q.append((a+dx[k], b+dy[k]))

    c = 0

    while(stack):
        a, b = stack.pop()
        arr[a][b] = 0
        c += 1

    return c

while(True):
    count = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                count = bfs(i, j)
                
                if count==0:
                    print(melt)
                    exit(0)
                else:
                    melt += 1
                    break

        if count: break
