from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(n, start, end):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((start, 0))

    while(queue):
        v, d = queue.popleft()

        if v[0] == end[0] and v[1] == end[1]:
            print(d)
            return

        for i in range(8):
            if 0 <= v[0]+dx[i] < n and 0 <= v[1]+dy[i] < n and visited[v[0]+dx[i]][v[1]+dy[i]] == 0:
                visited[v[0]+dx[i]][v[1]+dy[i]] = 1
                queue.append(((v[0]+dx[i], v[1]+dy[i]), d+1))

for i in range(t):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    bfs(n, (a, b), (c, d))
