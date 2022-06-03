from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)

def bfs():
    for i in range(n):
        q = deque()
        visited = [0 for _ in range(n)]
        q.append(i)
        visited[i] = 1
        dp[i][i] = 1

        while(q):
            v = q.popleft()

            for neighbor in adj[v]:
                if visited[neighbor]==0: 
                    dp[i][neighbor] = 1
                    visited[neighbor] = 1
                    q.append(neighbor)

bfs()
ans = 0

for i in range(n):
    sw = True

    for j in range(n):
        if dp[i][j] or dp[j][i]: continue
        else:
            sw = False
            break

    if sw: ans += 1

print(ans)키 순서
