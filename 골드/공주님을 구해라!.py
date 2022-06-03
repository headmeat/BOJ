from sys import stdin
import heapq
from collections import deque
input = stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 10**6
sword = -1

for i in range(n):
    for j in range(m):
        if arr[i][j]==2: sword = (i, j)

def bfs(sword):
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[sword[0]][sword[1]] = 1
    q.append((sword[0], sword[1], 0))

    while(q):
        x, y, c = q.popleft()
        
        if 0<=x+1<n and visited[x+1][y]==0: 
            q.append((x+1, y, c+1))
            visited[x+1][y] = c+1
        if 0<=y+1<m and visited[x][y+1]==0:
            q.append((x, y+1, c+1))
            visited[x][y+1] = c+1

    return visited[-1][-1]

def dijkstra_run(start):
    q = []

    heapq.heappush(q, (0, start[0], start[1]))
    dijkstra[start[0]][start[1]] = 0

    while(q):
        cost, x, y = heapq.heappop(q)

        if cost>dijkstra[x][y]: continue

        for k in range(4):
            if 0<=x+dx[k]<n and 0<=y+dy[k]<m and dijkstra[x+dx[k]][y+dy[k]] > cost + 1 and arr[x+dx[k]][y+dy[k]]!=1:
                dijkstra[x+dx[k]][y+dy[k]] = cost + 1
                heapq.heappush(q, (dijkstra[x+dx[k]][y+dy[k]], x+dx[k], y+dy[k]))

dijkstra = [[10**6 for _ in range(m)] for _ in range(n)]
dijkstra_run((0,0))
answer = min(dijkstra[-1][-1], dijkstra[sword[0]][sword[1]]+bfs(sword))

if answer<=t: print(answer)
else: print("Fail")
