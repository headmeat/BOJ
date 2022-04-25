from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())
arr = [[element for element in input().rstrip()] for _ in range(n)]
ans = 10**5

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global ans

    q = deque()
    visited = [[10**5 for _ in range(m)] for _ in range(n)]
    q.append((x, y, -1, -1))
    visited[x][y] = 0

    while(q):
        a, b, direction, count = q.popleft()

        for k in range(4):
            tmp = count if direction==k else count+1

            if 0<=a+dx[k]<n and 0<=b+dy[k]<m and tmp<=visited[a+dx[k]][b+dy[k]] and arr[a+dx[k]][b+dy[k]]!="*":
                visited[a+dx[k]][b+dy[k]] = tmp

                if k==direction:
                    q.append((a+dx[k], b+dy[k], k, count))
                else: 
                    q.append((a+dx[k], b+dy[k], k, count+1))

                if arr[a+dx[k]][b+dy[k]]=="C": ans = min(ans, tmp)

    print(ans)
    exit(0)

for i in range(n):
    for j in range(m):
        if arr[i][j]=="C":
            bfs(i, j)
