from sys import stdin
from collections import deque
input = stdin.readline

INF = 10 ** 15
n, m = map(int, input().split())
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[INF for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v, depth):
    queue = deque()
    queue.append((v, depth))
    visited[v[0]][v[1]] = 1

    while(queue):
        u, depth = queue.popleft()
        
        for i in range(4):
            if 0 <= u[0] + dx[i] < n and 0 <= u[1] + dy[i] < m and visited[u[0] + dx[i]][u[1] + dy[i]] == INF and arr[u[0] + dx[i]][u[1] + dy[i]] == 1:
                queue.append(((u[0] + dx[i], u[1] + dy[i]), depth + 1))
                if depth + 1 < visited[u[0] + dx[i]][u[1] + dy[i]]: visited[u[0] + dx[i]][u[1] + dy[i]] = depth + 1

bfs((0, 0), 1)

print(visited[n-1][m-1])
