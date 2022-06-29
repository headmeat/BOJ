from sys import stdin
from copy import deepcopy
from collections import deque
input = stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global visited, tmp

    q = deque()
    visited[x][y] = 1
    q.append((x, y))

    #새 배열에다 옮겨놔야 
    while(q):
        a, b = q.popleft()

        for k in range(4):
            if 0<=a+dx[k]<n and 0<=b+dy[k]<m:
                if arr[a+dx[k]][b+dy[k]]==0: 
                    if tmp[a][b]: tmp[a][b] -= 1
                elif visited[a+dx[k]][b+dy[k]]==0:
                    visited[a+dx[k]][b+dy[k]] = 1
                    q.append((a+dx[k], b+dy[k]))

    return

years = 0

while True:
    count = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    tmp = [x[:] for x in arr]

    for i in range(n):
        for j in range(m):
            if arr[i][j]>0 and visited[i][j]==0:
                bfs(i, j)
                count += 1
    
    arr = tmp

    if count == 0:
        print(0)
        exit(0)
    elif count>1: 
        print(years)
        exit(0)

    years += 1
