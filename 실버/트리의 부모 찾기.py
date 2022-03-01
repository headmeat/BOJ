import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0 for _ in range(n+1)]

def dfs(parent, v):
    for n in adj[v]:
        if visited[n] == 0:
            visited[n] = v
            dfs(v, n)

visited[1] = 1
dfs(1, 1)

for i in range(2, len(visited)):
    print(visited[i])
