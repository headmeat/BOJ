from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [[x for x in input().rstrip()] for _ in range(n)]
start = [-1, -1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 10**7

for i in range(n):
    for j in range(m):
        if arr[i][j] == "0": start = [i, j]

def solve():
    global ans

    q = deque()
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(64)]

    q.append((start[0], start[1], 0, 0))
    visited[0][start[0]][start[1]] = 1

    while(q):
        x, y, s, key = q.popleft()
        
        if arr[x][y] == "1":
            ans = min(ans, s)
            continue
        elif 97<=ord(arr[x][y])<=122: key = key|(int(2**(ord(arr[x][y])-97)))

        for k in range(4):
            if 0<=x+dx[k]<n and 0<=y+dy[k]<m and visited[key][x+dx[k]][y+dy[k]]==0 and arr[x+dx[k]][y+dy[k]]!="#":
                if 65<=ord(arr[x+dx[k]][y+dy[k]])<=90 and int(2**(ord(arr[x+dx[k]][y+dy[k]])+32-97))&key==0: continue

                visited[key][x+dx[k]][y+dy[k]] = 1
                q.append((x+dx[k], y+dy[k], s+1, key))

    return

solve()

if ans==10**7: print(-1)
else: print(ans)
