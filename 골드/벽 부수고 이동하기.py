from sys import stdin
from collections import deque
input = stdin.readline

INF = 10 ** 15
n, m = map(int, input().split())
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 10 ** 15

#c==0: 벽을 부수고 옴.
#c==1: 벽을 안 부수고 옴.

def bfs(v, depth, chance):
    global ans
    queue = deque()
    queue.append((v, depth, chance))
    visited[v[0]][v[1]][depth] = depth

    while(queue):
        u, d, c = queue.popleft()
        if u == (n-1, m-1): ans = min(ans, d)
        for i in range(4):
            if 0 <= u[0] + dx[i] < n and 0 <= u[1] + dy[i] < m and visited[u[0] + dx[i]][u[1] + dy[i]][c] == 0:
                if arr[u[0] + dx[i]][u[1] + dy[i]] == 0: 
                    queue.append(((u[0] + dx[i], u[1] + dy[i]), d + 1, c))
                    visited[u[0] + dx[i]][u[1] + dy[i]][c] = 1
                elif c > 0:
                    queue.append(((u[0] + dx[i], u[1] + dy[i]), d + 1, c-1))
                    visited[u[0] + dx[i]][u[1] + dy[i]][c] = 1

bfs((0, 0), 1, 1)

if sum(visited[n-1][m-1]) == 0: print(-1)
else: print(ans)
