from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y, d = map(int, input().split())
xx, yy, dd = map(int, input().split())
dx = [0, 0, 1, -1]
INF = 10**5
dy = [1, -1, 0, 0]
rotate = [1, 0, 3, 2]
ans = INF

x, y, d = x-1, y-1, d-1
xx, yy, dd = xx-1, yy-1, dd-1

q = deque()
visited = [[[INF for _ in range(4)] for _ in range(m)] for _ in range(n)]
visited[x][y][d] = 1
q.append((x, y, d, 0))

while(q):
    a, b, direction, c = q.popleft()

    if a==xx and b==yy:
        add = 0
        if rotate[dd] == direction: add = 2
        elif dd != direction: add = 1

        ans = min(ans, c+add)
        continue

    for i in range(4):
        add = 0
        if rotate[i]==direction: add = 2
        elif i!=direction: add = 1

        for k in range(1, 4):
            x_, y_ = a+dx[i]*k, b+dy[i]*k

            if 0<=x_<n and 0<=y_<m:
                if arr[x_][y_]==1: break
                elif c + add + 1 < visited[x_][y_][i]:
                    visited[x_][y_][i] = c + add + 1
                    q.append((x_, y_, i, c + add + 1))

print(ans)
