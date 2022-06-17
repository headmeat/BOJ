from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y):
    global ans, visited
    q = deque()
    q.append((x, y))

    while(q):
        a, b = q.popleft()
        
        for k in range(4):
            if 0<=a+dx[k]<n and 0<=b+dy[k]<m and visited[a+dx[k]][b+dy[k]]==0 and arr[a+dx[k]][b+dy[k]]==move[k]:
                q.append((a+dx[k], b+dy[k]))
                visited[a+dx[k]][b+dy[k]] = 1

move = ["D", "U", "R", "L"]
dx = [-1, 1, 0, 0]#U, D, L, R
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
arr = [[x for x in input().rstrip()] for _ in range(n)]

for i in range(m):
    if visited[0][i]==0: bfs(-1, i)
    if visited[n-1][i]==0: bfs(n, i)

for i in range(n):
    if visited[i][0]==0: bfs(i, -1)
    if visited[i][m-1]==0: bfs(i, m)

print(sum([sum(x) for x in visited]))
