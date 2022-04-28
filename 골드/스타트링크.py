from sys import stdin
from collections import deque
input = stdin.readline

f, s, g, u, d = map(int, input().split())
dp = [-1 for _ in range(f)]
c = 0

def bfs():
    q = deque()
    q.append((s-1, 0))
    visited = [0 for _ in range(f)]
    visited[s-1] = 1

    while(q):
        a, depth = q.popleft()

        if a==g-1:
            print(depth)
            exit(0)

        if 0<=a-d<f and visited[a-d]==0:
            q.append((a-d, depth+1))
            visited[a-d] = 1
        if 0<=a+u<f and visited[a+u]==0:
            q.append((a+u, depth+1))
            visited[a+u] = 1

bfs()
print("use the stairs")
